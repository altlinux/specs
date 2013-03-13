# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:          sugar-pippy
Version:       51
Release:       alt1_1
Summary:       Pippy for Sugar

Group:         Graphical desktop/Sugar
License:       GPLv2+
URL:           http://wiki.laptop.org/go/Pippy
Source0:       http://download.sugarlabs.org/sources/sucrose/fructose/Pippy/Pippy-%{version}.tar.bz2
BuildArch:     noarch

BuildRequires: python-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gettext
BuildRequires: sugar-toolkit-gtk3

Requires:      gobject-introspection
Requires:      sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
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
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.Pippy


%files -f org.laptop.Pippy.lang
%doc NEWS COPYING
%{sugaractivitydir}/Pippy.activity/


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 51-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 48-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 46-alt1_1
- new version; import from fc17 release

