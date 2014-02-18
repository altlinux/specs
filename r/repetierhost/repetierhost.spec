%define Name RepetierHost
Name: repetierhost
Version: 0.90D
Release: alt2
Summary: 3D printer control software
License: ASL 2.0
URL: http://www.repetier.com/
Group: Engineering
Source0: %name-%version.tar
Source1: %{name}.desktop
BuildRequires: mono-devel mono-winforms opentk
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: /proc
BuildRequires: font(freesans)
Requires: font(freesans)

%description
Software for controlling RepRap style 3D-printer like Mendel, Darwin or Prusa
Mendel. Works with most firmware types. It is optimized to work with
Repetier-Firmware Other working firmware is Sprinter, Teacup, Marlin and all
compatible firmwares.

%prep
%setup -q
# # Drop Slic3r and OpenTK licenses
# head -16 Repetier-Host-licence.txt > Repetier-Host-licence.txt.short \
# && mv -f Repetier-Host-licence.txt.short Repetier-Host-licence.txt
dos2unix Repetier-Host-licence.txt README* changelog.txt

#Linux splashscreen
cp -f linux/hostsplash.png src/data/splashscreen.png

cd src/%Name

# Linux is case sensitive
sed -i 's/ColorSlider.designer.cs/ColorSlider.Designer.cs/' %{Name}.csproj

# Overwrite Arial with something more free
sed -i 's/Arial/FreeSans/g' view/utils/ArrowButton.cs view/RepetierEditor.Designer.cs view/PrintPanel.Designer.cs

cd -

%build
cd src/%Name
xbuild %{Name}.sln /p:Configuration=Release || xbuild %{Name}.sln /p:Configuration=Release
cd -

%install
mkdir -p %buildroot%_monodir/%Name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%Name
mkdir -p %buildroot%_datadir/applications
mkdir -p %buildroot%_datadir/pixmaps

cp src/%Name/bin/Release/%{Name}* %buildroot%_monodir/%Name
cp -r src/data/* %buildroot%_datadir/%Name
ln -s %_datadir/%Name %buildroot%_monodir/%Name/data
cp src/%Name/repetier-logo-trans32.ico %buildroot%_datadir/pixmaps/%{Name}.ico

desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1

cat <<EOF > %buildroot%_bindir/%name
#!/usr/bin/env bash
mono /usr/lib/mono/%Name/%{Name}.exe
exit $?
EOF

chmod +x %buildroot%_bindir/%name

%files
%doc APACHE-LICENSE-2.0.txt Repetier-Host-licence.txt README* changelog.txt
%_monodir/%Name
%_bindir/%name
%_datadir/%Name
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{Name}.ico

%changelog
* Tue Feb 18 2014 Dmitry Derjavin <dd@altlinux.org> 0.90D-alt2
- Possible xbuild race workaround.

* Thu Feb 13 2014 Dmitry Derjavin <dd@altlinux.org> 0.90D-alt1
- Initial ALTLinux build.
