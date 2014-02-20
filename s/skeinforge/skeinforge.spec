
Name:           skeinforge
Version:        12.03.14
Release:        alt1
Summary:        Converts 3D model into G-Code for RepRap
# Asked author for LICENSE file - will be in next release
# Dev version for check: http://members.axion.net/~enrique/reprap_python_beanshell.zip
# Don't ask me, why the dev version isn't on the same website :(
License:        AGPLv3
Group:          Engineering
URL:            http://fabmetheus.crsndoo.com/wiki/index.php/Skeinforge
Source0:        http://fabmetheus.crsndoo.com/files/50_reprap_python_beanshell.zip
Source1:        %{name}.desktop
Source2:        %{name}
Source3:        %{name}-craft
Patch0:         %{name}-remove-tkinter-warning.patch
Patch1:         %{name}-comb.patch
Patch2:         %{name}-cool.patch
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  desktop-file-utils
BuildRequires:  unzip
#Requires:       pypy
#Requires:       python-modules-tkinter

%description
Skeinforge is a tool chain composed of Python scripts that converts your
3D model into G-Code instructions for RepRap.

%package        doc
Group:          Engineering
Requires:       %{name} = %{version}-%{release}
Summary:        Documentation for %{name}

%description    doc
Skeinforge is a tool chain composed of Python scripts that converts your
3D model into G-Code instructions for RepRap.
This is the documentation.

%prep
%setup -cq
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Removing stupid useless files
rm -rf %{name}_application/*.sh %{name}_application/*.stl

# Removing shebangs
cd %{name}_application/%{name}_plugins/craft_plugins/
for FILE in preface.py alteration.py bottom.py dimension.py fill.py inset.py limit.py scale.py widen.py; do
  awk 'FNR>1' $FILE > $FILE.nobang && mv -f $FILE.nobang $FILE
done
cd -

cd fabmetheus_utilities/miscellaneous/fabricate/
for FILE in example.py send.py RepRapArduinoSerialSender.py; do
  awk 'FNR>1' $FILE > $FILE.nobang && mv -f $FILE.nobang $FILE
done
chmod +x frank_davies/t.sh
cd -

# Fix utilites module name
subst 's/skeinforge_tools.skeinforge_utilities/fabmetheus_utilities/' fabmetheus_utilities/miscellaneous/fabricate/extrude.py

%build

%install
mkdir -p %buildroot%python_sitelibdir/%name
mkdir -p %buildroot%_bindir
cp -ar [fs_]* %buildroot%python_sitelibdir/%name
desktop-file-install --dir=%buildroot%_desktopdir %SOURCE1 # desktop file
cp -a %SOURCE2 %SOURCE3 %buildroot%_bindir # launchers

%files
%doc
%_bindir/%{name}*
%python_sitelibdir/%name
%_desktopdir/%name.desktop

%files      doc
%doc documentation

%changelog
* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 12.03.14-alt1
- Import from Fedora
