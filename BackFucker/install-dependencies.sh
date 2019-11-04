echo "[ Backfucker - Dependencies Installer]"

echo""
echo""

apt-get update
apt-get install python
echo""
echo""

echo"[Downloading - Pyfiglet ]"
echo""

git clone https://github.com/pwaller/pyfiglet

echo""
echo""



echo "[Installing - Pyfiglet ]"
echo""
cd pyfiglet
python setup.py install

echo ""
echo ""

echo"All Dependencies are Installed . Enjoy :)"
echo""

echo "Ps- to open bacfucker type this on your terminal: "
echo" chmod +x bacfucker.py"
echo "run with ./bacfucker.py"

