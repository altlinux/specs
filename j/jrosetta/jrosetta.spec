Name: jrosetta
Version: 1.0.2
Release: alt2
Summary: A common base to build a graphical console

Group: Development/Java
License: GPLv2
Url: http://dev.artenum.com/projects/JRosetta/
#http://dev.artenum.com/projects/JRosetta/download/JRosetta-1-0-2/data/src-gpl?action=download&nodecorator
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-gpl.tar

BuildArch: noarch

BuildRequires: rpm-build-java ant

%description
JRosetta provides a common base for graphical component that could be used
to build a graphical console in Swing with the latest requirements, such as
command history, completion and so on for instance for scripting language
or command line.

%prep
%setup -q -n %name-%version-gpl
#wrong-file-end-of-line-encoding
cp -p CHANGE.txt CHANGE.txt.CRLF
%__subst 's/\r//' CHANGE.txt
touch -r CHANGE.txt.CRLF CHANGE.txt
rm CHANGE.txt.CRLF

%build
%ant make

%install
mkdir -p %buildroot%_javadir

for j in jrosetta-API jrosetta-engine ; do
  install -pm 0644 dist/${j}.jar %buildroot%_javadir/${j}-%version.jar
  ln -fs ${j}-%version.jar %buildroot%_javadir/${j}.jar
done

%files
%doc CHANGE.txt COPYRIGHT LICENSE.txt
%_javadir/jrosetta*.jar

%changelog
* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2
- Fix BuildRequires (ALT #21518)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 kwizart < kwizart at gmail.com > - 1.0.2-1
- Fix License (GPLv2 only)
- Fix Summary
- Update to 1.0.2 - previous patch merged upstream

* Mon Oct 27 2008 kwizart < kwizart at gmail.com > - 1.0.1-1
- Initial Package

