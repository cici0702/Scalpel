from scalpel.import_graph.import_graph import Tree,ImportGraph

root_node = Tree("import_graph_example_pkg")
import_graph = ImportGraph()
import_graph.build_dir_tree(root_node)
module_dict = import_graph.parse_import(root_node)

