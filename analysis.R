library(ggplot2)
setwd("/Users/mattia/Desktop/AI_ass3/clustering")

sp_rand_cluster <- read.delim("spectral_rand_cluster.txt", header = TRUE, 
                              sep = "\t", dec = ".")

lca_rand_cluster <- read.delim("lca_rand_cluster.txt", header = TRUE, 
                              sep = "\t", dec = ".")
ms_rand_cluster <- read.delim("meanshift_rand_cluster.txt", header = TRUE, 
                               sep = "\t", dec = ".")
pdf("full_randIndex.pdf")
ggplot() + 
  geom_line(data=sp_rand_cluster, aes( x=k_cluster, y=rand_index, 
                                       colour="Spectral Clustering" ), size=2) +
  geom_line(data=lca_rand_cluster, aes( x=k_cluster, y=rand_index, 
                                       colour="LCA" ), size=2) +
  geom_line(data=ms_rand_cluster, aes( x=k_cluster, y=rand_index, 
                                        colour="Mean Shift" ), size=2) +
  scale_color_manual("",
                   breaks = c("Spectral Clustering", "Mean Shift", "LCA"), 
                   values = c("darkcyan", "springgreen3", "gold"))+
  scale_x_continuous(breaks = seq(5,23,3))+
  scale_y_continuous(breaks = seq(0.6, 1, 0.05))+
  theme(legend.position = c(0.9, 0.1))+ 
  theme(legend.key.size = unit(0.4, "cm"), legend.title = element_blank())+
  labs(title="", y="Rand Index", x="Number of Cluster")
dev.off()

#### Mean Shift with different PCA features ####################################
pca2 <- read.delim("meanshift_rand_cluster_pca2.txt", header = TRUE, 
                   sep = "\t", dec = ".")
pca4 <- read.delim("meanshift_rand_cluster_pca4.txt", header = TRUE, 
                   sep = "\t", dec = ".")
pca6 <- read.delim("meanshift_rand_cluster_pca6.txt", header = TRUE, 
                   sep = "\t", dec = ".")
pca10 <- read.delim("meanshift_rand_cluster_pca10.txt", header = TRUE, 
                   sep = "\t", dec = ".")
x_axis <- seq(31, 21, -1)/10

## bandwidth vs num of clusters
ggplot() + 
  geom_line(data=pca2, aes( x=x_axis, y=rev(k_cluster), 
                                       colour="2 features" ), size=2) +
  geom_line(data=pca4, aes( x=x_axis, y=rev(k_cluster), 
                                        colour="4 features" ), size=2) +
  geom_line(data=pca6, aes( x=x_axis, y=rev(k_cluster), 
                                       colour="6 features" ), size=2) +
  geom_line(data=pca10, aes( x=x_axis, y=rev(k_cluster), 
                                       colour="10 features" ), size=2) +
  scale_color_manual("",
                     breaks = c("2 features", "4 features", "6 features", "10 features"), 
                     values = c("red3", "green3", "darkorange", "blue2"))+
  scale_y_continuous(breaks = seq(0, 300, 30)) +
  scale_x_continuous(breaks = seq(2.0, 3.2, 0.1)) +
  #theme(legend.position = c(0.9, 0.1))+ 
  theme(legend.key.size = unit(0.4, "cm"), legend.title = element_blank()) +
  labs(title="", y="Number of cluster", x="Bandwidth")

## bandwidth vs rand index
ggplot() + 
  geom_line(data=pca2, aes( x=x_axis, y=rev(rand_index), 
                            colour="2 features" ), size=2) +
  geom_line(data=pca4, aes( x=x_axis, y=rev(rand_index), 
                            colour="4 features" ), size=2) +
  geom_line(data=pca6, aes( x=x_axis, y=rev(rand_index), 
                            colour="6 features" ), size=2) +
  geom_line(data=pca10, aes( x=x_axis, y=rev(rand_index), 
                             colour="10 features" ), size=2) +
  scale_color_manual("",
                     breaks = c("2 features", "4 features", "6 features", "10 features"), 
                     values = c("red3", "green3", "darkorange", "blue2")) +
  scale_x_continuous(breaks = seq(2.0, 3.2, 0.1)) +
  #scale_y_continuous(breaks = seq(0.1, 1.1, 0.1)) + 
  theme(legend.position = c(0.9, 0.1))+ 
  theme(legend.key.size = unit(0.4, "cm"), legend.title = element_blank()) +
  labs(title="", y="Rand Index", x="Bandwidth")


# k cluster vs rand index
pca2K <- read.delim("meanshift_rand_cluster_pca2.txt", header = TRUE, 
                   sep = "\t", dec = ".")
pca4K <- read.delim("meanshift_rand_cluster_pca4_band62-40.txt", header = TRUE, 
                   sep = "\t", dec = ".")
pca6K <- read.delim("meanshift_rand_cluster_pca6_band74-52.txt", header = TRUE, 
                   sep = "\t", dec = ".")
pca10K <- read.delim("meanshift_rand_cluster_pca10_band90-70.txt", header = TRUE, 
                    sep = "\t", dec = ".")
ggplot() + 
  geom_line(data=pca2K, aes( x=k_cluster, y=rand_index, 
                            colour="2 features" ), size=2) +
  geom_line(data=pca4K, aes( x=k_cluster, y=rand_index, 
                            colour="4 features" ), size=2) +
  geom_line(data=pca6K, aes( x=k_cluster, y=rand_index, 
                            colour="6 features" ), size=2) +
  geom_line(data=pca10K, aes( x=k_cluster, y=rand_index,  
                             colour="10 features" ), size=2) +
  scale_color_manual("",
                     breaks = c("2 features", "4 features", "6 features", "10 features"), 
                     values = c("red3", "green3", "darkorange", "blue2")) +
  scale_x_continuous(breaks = seq(0, 30, 3)) +
  #scale_y_continuous(breaks = seq(0, 1.1, 0.1)) + 
  theme(legend.position = c(0.9, 0.1))+ 
  theme(legend.key.size = unit(0.4, "cm"), legend.title = element_blank()) +
  labs(title="", y="Rand Index", x="Number of Clusters")

####



















