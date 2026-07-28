Name:           dita-ot
Version:        4.4
Release:        alt1

Summary:        DITA Open Toolkit - DITA-based XML publishing toolkit
License:        Apache-2.0
Group:          Development/Documentation
Url:            https://github.com/dita-ot/dita-ot
BuildArch:      noarch

Source:         %name-%version.tar.bz2

BuildRequires(pre): rpm-build-licenses

Requires:       java

%description
DITA Open Toolkit (DITA-OT) is a Java-based open source toolkit that
transforms DITA content into different output formats, including HTML,
WebHelp, PDF, and Eclipse Help.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_datadir/%name
cp -a bin lib plugins config resources \
      build.xml integrator.xml catalog-dita.xml \
      %buildroot%_datadir/%name/

# Drop unused launchers: bin/ant is a stock jpackage Ant wrapper (it runs
# plain Ant, not the DITA-OT invoker) whose shell.req emits bogus Requires
# on /etc/ant.conf, /usr/bin/build-classpath and /usr/share/java-utils; the
# .bat files are Windows-only. DITA-OT is driven solely via bin/dita, which
# launches org.apache.tools.ant.launch.Launcher straight from the bundled
# lib/ant-launcher.jar, so these are dead weight.
rm %buildroot%_datadir/%name/bin/ant \
   %buildroot%_datadir/%name/bin/ant.bat \
   %buildroot%_datadir/%name/bin/dita.bat

install -d %buildroot%_bindir
ln -s ../share/%name/bin/dita %buildroot%_bindir/dita

%files
%_bindir/dita
%_datadir/%name/
%doc LICENSE NOTICES.txt
%doc doc/

%changelog
* Wed Jul 08 2026 Valery Sinelnikov <greh@altlinux.org> 4.4-alt1
- Initial build for ALT Linux Sisyphus.
