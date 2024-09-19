  G = nx.Graph()


  # Add edges to the graph (connections)
  
 
  
  
  for _, row in df_graph.iterrows():
   G.add_edge(row['Madde_Kod'], row['Tr-Kod'])
 
  for node in G.nodes():
   if node in df_tr2:
    i=1
    z=0
    weight= df_w.loc[df_w['Tr-Kod']==node].copy()
    weight = weight['W_Toplam'].values.tolist()[0] 
    G.add_node(node, label= str(node), value=weight, pos=(i,z))  # Adjust the multiplier as needed
    
    i=i+1
    z=z+1
   else :
    G.add_node(node, label= str('-'), value=1)  # Adjust the multiplier as needed
 
 
  
  net = Network(height="270px", width="100%", bgcolor="#222222", font_color="white")


  # Load the networkx graph into PyVis
  net.from_nx(G)
  #g_sizes.add_node(i,label=str(i),value=val)
 
   
   # Customize the network
  #net.show_buttons(filter_=['physics'])  # Add options for interacting with the graph 


  net.set_options("""
   var options = {
    "nodes": {
      "color": {
        "highlight": {
          "border": "white",
          "background": "skyblue"
        }
      },
      "font": {
        "size": 16,
        "color": "white"
      },
      "scaling": {
        "min": 1,
        "max": 75
      }
    },
    "edges": {
      "color": {
        "color": "skyblue",
        "highlight": "white"
      },
      "smooth": {
        "enabled": true,
        "type": "dynamic"
      }
    },
    "interaction": {
      "hover": true
    },
    "physics": {
      "enabled": false
    }
  }
  """)
  
  
  # Generate and save the graph as an HTML file
  yol='C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\Python39\\network.html'
  yol='C:\\temp\\network.html'
  net.save_graph(yol)
  
  time.sleep(10)
  
  
  # Display the graph in Streamlit
  HtmlFile = open(yol, 'r', encoding='utf-8')
  with col3:
   components.html(HtmlFile.read(), height=270)
