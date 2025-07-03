# 🌾 ROS 2 + Gazebo Ignition: Simulação de Ambiente Agrícola com Docker

Este repositório contém um ambiente de simulação agrícola utilizando **ROS 2** e **Gazebo Ignition**, empacotado em um contêiner **Docker** para facilitar a portabilidade.

> ✅ Desenvolvido para facilitar testes e integração de robôs móveis em cenários agrícolas simulados.

---

## 📦 Estrutura

```
ros2_gazebo_docker_farm/
├── Dockerfile
├── moray_assets/
│   └── farm_inspection/
│       ├── launch/
│       ├── models/
│       ├── scripts/
│       ├── src/
│       ├── package.xml
│       └── CMakeLists.txt
```

---

## 🚀 Como Rodar (Ubuntu 20.04 limpo)

### 👣 1. Atualize o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

### 👣 2. Instale dependências

```bash
sudo apt install -y curl git gnupg2 lsb-release ca-certificates software-properties-common
```

### 👣 3. Instale o Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Adicione seu usuário ao grupo `docker`:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Verifique:

```bash
docker --version
```

---

### 👣 4. Clone este repositório

**Via HTTPS**:

```bash
git clone https://github.com/milenafariap/ros2_gazebo_docker_farm.git
cd ros2_gazebo_docker_farm
```

---

### 👣 5. Construa a imagem Docker

```bash
docker build -t ros2_gz_farm .
```

---

### 👣 6. Configure o acesso gráfico (X11)

No terminal do **host**:

```bash
xhost +local:docker
```

---

### 👣 7. Execute o contêiner

```bash
docker run -it --rm \
  -v ~/ros2_gazebo_docker_farm:/root/moray \
  -e GZ_SIM_RESOURCE_PATH=/root/moray/moray_assets/sdf_world \
  -e GAZEBO_MODEL_PATH=/root/moray/moray_assets/models \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --network host \
  ros2_gz_farm
```

---

### 👣 8. Compile e rode dentro do contêiner

```bash
cd /root/moray
colcon build
source install/setup.bash
ros2 launch farm_inspection gazebo_with_bridge.launch.py
```

✅ Isso abrirá o mundo `.sdf` no Gazebo Ignition com pontes ROS 2 ativas.

---

## 🔹 Modo Alternativo: Rodar somente o mundo `.sdf`

Caso queira apenas abrir o mundo sem ROS 2:

### Dentro do contêiner:

```bash
ign gazebo /root/moray/moray_assets/farm_inspection/models/building_robot.sdf --verbose
```

Ou se estiver no host com Ignition instalado:

```bash
ign gazebo path/to/building_robot.sdf --verbose
```

---

## 🧪 Testes rápidos

Reabrir o contêiner:

```bash
docker start -ai ros2_gz
```

Remover e recriar limpo:

```bash
docker rm -f ros2_gz
docker run ... # (repita o comando completo)
```

---

## 🔒 Segurança

Ao terminar:

```bash
xhost -local:docker
```

---

## 📌 Requisitos

- Ubuntu 20.04+
- Docker e permissão para usar GPU (se desejar)
- Interface gráfica ativa (X11) para visualização do Gazebo
