# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		arduino
Epoch:		1
Version:	1.0.6
Release:	alt1_3jpp8
Summary:	An IDE for Arduino-compatible electronics prototyping platforms
Group:		Development/Java
License:	GPLv2+ and LGPLv2+ and CC-BY-SA
URL:		http://www.arduino.cc/

# There are lots of binaries in the "source" tarball.  Remove them with:
# version=1.0.6; curl -L https://github.com/arduino/Arduino/archive/$version.tar.gz | tar -xzf - && mv Arduino-$version arduino-$version && rm -r arduino-$version/build/linux/dist/tools/* && rm -r arduino-$version/hardware/arduino/firmwares/wifishield && find arduino-$version \( -type d \( -name macosx -o -name windows \) -o -type f \( -iname '*.jar' -or -iname '*.tgz' -or -iname '*.tar.gz' -or -iname '*.so' \) \) -print0 | xargs -0 rm -rf && tar -cJf arduino-$version.tar.xz arduino-$version
# See also http://code.google.com/p/arduino/issues/detail?id=193
Source0:	%{name}-%{version}.tar.xz

BuildArch:	noarch

# Use unbundled libs:
Patch0:		arduino-script.patch
Patch7:		arduino-no-avrdude64.patch
# Requested upstream in http://github.com/arduino/Arduino/pull/5:
Patch3:		arduino-use-system-rxtx.patch

# Requested upstream in http://github.com/arduino/Arduino/pull/6:
Patch4:		arduino-icons-etc.patch

Patch6:		arduino-add-to-groups.patch

# Required for Koji's ARM build hosts:
Patch8:		arduino-build-platform.patch

# Requested upstream in https://github.com/arduino/Arduino/pull/1572:
Patch9:         arduino-appdata.patch

# Accepted upstream for Arduino 1.5.
Patch10:        0001-Handle-new-.ino-file-extension-on-Linux.patch

BuildRequires:	jpackage-utils ant ant-apache-regexp desktop-file-utils ecj jna rxtx git
Requires:	%{name}-core = %{epoch}:%{version}-%{release} %{name}-doc = %{epoch}:%{version}-%{release}
Requires:	fonts-type1-xorg ecj jna rxtx
Requires:	zenity perl polkit
Source44: import.info


%description
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains an IDE that can be used to develop and upload code
to the micro-controller.


%package -n %{name}-core
Summary:	Files required for compiling code for Arduino-compatible micro-controllers
Group:		Development/Java
Requires:	avr-gcc avr-gcc-c++ avr-libc avrdude


%description -n %{name}-core
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains the core files required to compile and upload
Arduino code.


%package -n %{name}-doc
Summary:	Documentation for the Arduino micro-controller platform
Group:		Development/Java
Requires:	avr-gcc avr-gcc-c++ avr-libc avrdude


%description -n %{name}-doc
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains reference documentation.


%prep
%setup -q -n %{name}-%{version}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch6 -p1
chmod a+rx build/linux/%{name}-add-groups
%patch0
%patch3 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1

echo -e "\n# By default, don't notify the user of a new upstream version." \
        "\n# https://bugzilla.redhat.com/show_bug.cgi?id=773519" \
        "\nupdate.check=false" \
    >> build/shared/lib/preferences.txt

git apply %{PATCH4}

%patch10 -p1

build-jar-repository -p -s app/lib/ ecj jna RXTXcomm


%build
cd core/methods
ant
cd ..
ant
cd ../build
echo %{version} | ant dist
tar -xf linux/%{name}-%{version}-linux.tgz


%install
cd build/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -a arduino $RPM_BUILD_ROOT/%{_bindir}/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a hardware lib libraries examples $RPM_BUILD_ROOT/%{_datadir}/%{name}/
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/lib/*.jar
rm -r $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/tools

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
cp -a ../../license.txt ../../README.md reference $RPM_BUILD_ROOT/%{_docdir}/%{name}/
ln -s %{_docdir}/%{name}/reference $RPM_BUILD_ROOT/%{_datadir}/%{name}/reference

# Requested upstream in http://github.com/arduino/Arduino/pull/4:
find $RPM_BUILD_ROOT -type f -iname *.jpg -or -iname *.java -or -iname *.pde -or -iname *.h -or -iname *.cpp -or -iname *.c -or -iname *.txt -or -iname makefile -or -iname key*.txt -or -iname pref*.txt | xargs chmod -x;

cp -a lib/core.jar lib/pde.jar $RPM_BUILD_ROOT/%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/boards.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/programmers.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/lib/preferences.txt \
   $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/
ln -s %{_sysconfdir}/%{name}/boards.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/boards.txt
ln -s %{_sysconfdir}/%{name}/programmers.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/programmers.txt
ln -s %{_sysconfdir}/%{name}/preferences.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/lib/preferences.txt

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp -p ../linux/%{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ../linux/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime/packages
cp -a ../linux/%{name}.xml $RPM_BUILD_ROOT/%{_datadir}/mime/packages/

for dir in ../linux/icons/*; do
    size=`basename $dir`
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/$size/apps
    cp $dir/%{name}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/$size/apps/
done

mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}
cp -a ../linux/%{name}-add-groups $RPM_BUILD_ROOT/%{_libexecdir}/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/polkit-1/actions
cp -a ../linux/cc.arduino.add-groups.policy $RPM_BUILD_ROOT/%{_datadir}/polkit-1/actions

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/appdata
cp -a ../linux/%{name}.appdata.xml $RPM_BUILD_ROOT/%{_datadir}/appdata/
# unFedorize; ALTize
if grep 'dialout lock' %buildroot/%_bindir/arduino; then
   sed -i -e 's,dialout lock,uucp,' %buildroot/%_bindir/arduino
else
   echo "ALT-specific group hack is deprecated"
   exit 2
fi



%files
%{_bindir}/*
%{_datadir}/%{name}/*.jar
%{_datadir}/%{name}/lib/*
%exclude %{_datadir}/%{name}/lib/version.txt
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy
%{_libexecdir}/%{name}-add-groups
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/reference
%{_datadir}/appdata/%{name}.appdata.xml


%files -n %{name}-core
%{_docdir}/%{name}/license.txt
%{_docdir}/%{name}/README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/boards.txt
%config(noreplace) %{_sysconfdir}/%{name}/programmers.txt
%config(noreplace) %{_sysconfdir}/%{name}/preferences.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/hardware/
%{_datadir}/%{name}/libraries/
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/version.txt


%files -n %{name}-doc
%{_docdir}/%{name}/


%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.6-alt1_3jpp8
- new version

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.0.6-alt1_3jpp7
- update to new release by jppimport

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.5-alt1_7jpp7
- update to new release by jppimport

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.5-alt1_6jpp7
- update

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.5-alt1_4jpp7
- update to new release by jppimport

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.0.1-alt2_4jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for arduino-core

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_4jpp7
- fc update

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_3jpp7
- update to new release by jppimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_1jpp7
- applied repocop patches

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_1jpp7
- new version

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_5jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_4jpp6
- update to new release by jppimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_3jpp6
- import by jppimport

