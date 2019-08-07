Group: Sciences/Physics
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             gresistor
Version:          0.0.2
Release:          alt1_10
Summary:          Gnome resistor color code calculator

License:          GPL+
URL:              https://sourceforge.net/projects/gresistor/

Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    python-devel desktop-file-utils

Requires:         python-module-pygtk-libglade
Requires:         tepache
Source44: import.info


%description
To allow for identification, resistors are usually marked with
colored bands. Often refereed to as color codes, these markings
are indicative of their resistance, tolerance and temperature
coefficient. gResistor is a great program that will help you
translate a resistor color codes into a readable value.


%prep
%setup -q


# Remove bundled SimpleGladeApp.py
rm -f SimpleGladeApp.py
sed -i '/py_modules =/d' setup.py


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


desktop-file-install \
    --remove-key=Version                        \
    --remove-key=Encoding                       \
    --add-category "Science;Engineering"          \
    --delete-original                           \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/%{name}.desktop



%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{python_sitelibdir_noarch}/%{name}-%{version}-py?.?.egg-info


%changelog
* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_10
- update to new release by fcimport

* Thu Jul 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1
- new version (closes: #37018)

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt3.1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gresistor
  * postclean-03-private-rpm-macros for the spec file

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt3.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3.1
- Rebuilt with python 2.6

* Thu Apr 03 2008 Mikhail Pokidko <pma@altlinux.org> 0.0.1-alt3
- repocop fixes

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 0.0.1-alt2.1
- Rebuilt with python-2.5.

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 0.0.1-alt2
- Build as noarch.
- Use python_sitelibdir macro while packaging.

* Mon Sep 11 2006 Mikhail Pokidko <pma@altlinux.org> 0.0.1-alt1
- Initial package.
