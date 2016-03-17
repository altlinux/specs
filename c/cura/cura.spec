%global commit 95c2af21db7fdda8c4324a923fa004859f6c5b9c

Name:           cura
Version:        15.04.4
Release:        alt2
Summary:        3D printer control software

Group:		Other
# Code is AGPLv3
# Icons AGPLv3 https://github.com/daid/Cura/issues/231#issuecomment-12209683
# Example models are CC-BY-SA
# TweakAtZ.py is CC-BY-SA
License:        AGPLv3 and CC-BY-SA

URL:            https://github.com/daid/Cura

BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install

# I've stripped the source with the script in Source3
# To remove CC BY-NC content
# Upstream not willing to ship free package
Source0:        Cura-%{commit}-fedora.tar.gz
Source1:        %{name}
Source2:        %{name}.desktop
Source3:        %{name}-stripper.sh

# UltimakerPlatforms STLs were stripped from the tarball, don't crash because of that
Patch0:         %{name}-dont-show-nc-stls.patch

# Use system paths
Patch1:         %{name}-system-paths.patch

# Rework the logic of determining the version (didn't work)
Patch2:         %{name}-version.patch

# Disable installation of firmwares Fedora doesn't ship
Patch3:         %{name}-no-firmware.patch

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-OpenGL
BuildRequires:  python-module-numpy
BuildRequires:  python-module-power
BuildRequires:  python-module-serial
BuildRequires:  python-module-wx-devel
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires: 	python-module-numpy-addons python-module-numpy-testing
Requires:       CuraEngine >= 15.04

%description
Cura is a project which aims to be an single software solution for 3D
printing.  While it is developed to be used with the Ultimaker 3D
printer, it can be used with other RepRap based designs.

Cura helps you to setup an Ultimaker, shows your 3D model, allows for
scaling / positioning, can slice the model to G-Code, with sane editable
configuration settings and send this G-Code to the 3D printer for
printing.

%prep
%setup -qn Cura-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

dos2unix resources/example/Attribution.txt

sed -i 's/REPLACE_THIS_IN_SPEC/%{version}/' Cura/util/version.py

%build
# rebuild locales
cd resources/locale
rm *.in *.pot
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/Cura.po -o $FILE/LC_MESSAGES/Cura.mo
  rm $FILE/LC_MESSAGES/Cura.po
done
cd -

%install
mkdir -p %{buildroot}%{python_sitelibdir_noarch}/Cura
mkdir -p %{buildroot}%{_datadir}/%{name}/firmware
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_bindir}

cp -apr Cura/* %{buildroot}%{python_sitelibdir_noarch}/Cura
rm -rf %{buildroot}%{python_sitelibdir_noarch}/Cura/LICENSE
cp -apr resources/* %{buildroot}%{_datadir}/%{name}
cp -apr plugins %{buildroot}%{_datadir}/%{name}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name} %{buildroot}%{python_sitelibdir_noarch}/Cura/resources
ln -s %{_datadir}/%{name}/%{name}.ico %{buildroot}%{_datadir}/pixmaps

# locales
cp -ar %{buildroot}%{_datadir}/%{name}/locale/* %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{_datadir}/%{name}/locale
ln -s -f %{_datadir}/locale/ %{buildroot}%{_datadir}/%{name}/ # the app expects the locale folder in here

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%{find_lang} Cura

%files -f Cura.lang
%doc Cura/LICENSE resources/example/Attribution.txt
%python_sitelibdir_noarch/Cura
%_bindir/%name
%_datadir/%name
%_pixmapsdir/%name.ico
%_desktopdir/%name.desktop

%changelog
* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 15.04.4-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt1_2
- update to new release by fcimport

* Thu Nov 26 2015 Igor Vlasenko <viy@altlinux.ru> 15.02.1-alt1_4
- new version

