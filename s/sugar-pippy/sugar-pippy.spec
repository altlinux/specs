# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name:           sugar-pippy
Version:        48
Release:        alt1_1
Summary:        Pippy for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Pippy
Source0:        http://download.sugarlabs.org/sources/sucrose/fructose/Pippy/Pippy-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
BuildRequires:  gettext

Requires:       sugar
Requires:       python-module-pygame
Requires:       python-module-pybox2d
Requires:       python-module-elements
Source44: import.info
Obsoletes: sugar-pippy-activity < %version
Conflicts: sugar-pippy-activity < %version


%description
Teaches Python programming by providing access to Python code samples
and a fully interactive Python interpreter.

The user can type and execute simple Python expressions. For example,
it would be possible for a user to write Python statements to calculate
expressions, play sounds, or make simple text animation. 


%prep
%setup -q -n Pippy-%{version}
# Fix permissions
rm -rf library/pippy/physics

# Remove shebang
for Files in pippy_app.py ; do
  %{__sed} -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  %{__rm} ${Files}.orig
done


%build
%{__python} setup.py build


%install
%{__python} setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.Pippy


%files -f org.laptop.Pippy.lang
%doc NEWS
%{sugaractivitydir}/Pippy.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 48-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 46-alt1_1
- new version; import from fc17 release

