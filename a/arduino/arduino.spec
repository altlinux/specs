# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		arduino
Epoch:		1
Version:	1.6.4
Release:	alt1_8jpp8
Summary:	An IDE for Arduino-compatible electronics prototyping platforms
Group:		Development/Java
License:	GPLv2+ and LGPLv2+ and CC-BY-SA
URL:		http://www.arduino.cc/

# There are a lot of binaries in the "source" tarball.
# These binaries are removed in the prep section of the SPEC file.
Source0:	https://github.com/arduino/Arduino/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	java-devel >= 1.8.0
BuildRequires:	jpackage-utils ant ant-apache-regexp desktop-file-utils ecj jna
BuildRequires:	jmdns jsemver apache-commons-net apache-commons-codec git
BuildRequires:	apache-commons-compress apache-commons-exec apache-commons-lang3
BuildRequires:	apache-commons-logging jsch guava jackson-annotations jssc
BuildRequires:	bouncycastle-pg jackson-databind jackson-module-mrbean
BuildRequires:	jakarta-commons-httpclient objectweb-asm
Requires:	java >= 1.8.0
Requires:	fonts-type1-xorg ecj jna zenity perl polkit ecj jna
Requires:	jmdns jsemver apache-commons-net apache-commons-codec git
Requires:	apache-commons-compress apache-commons-exec apache-commons-lang3
Requires:	apache-commons-logging jsch guava jackson-annotations jssc
Requires:	bouncycastle-pg jackson-databind jackson-module-mrbean
Requires:	jakarta-commons-httpclient objectweb-asm libastyle-devel
Requires:	%{name}-core = %{epoch}:%{version} %{name}-doc = %{epoch}:%{version}

# This patch skips the init process for OSX platforms.
Patch0:		arduino-macosx.patch
# Turns off all network downloads in build
Patch1:		arduino-no-network.patch
# Redirects Arduino to system avr-gcc and avrdude utilities
Patch2:		arduino-use-system-avrdude.patch
Patch3:		arduino-add-to-groups.patch
Patch4:		arduino-script.patch
# Redirects Arduino to system astyle libraries
Patch5:		arduino-use-system-astyle.patch
# Allows Arduino to build on non-intel systems
Patch6:		arduino-armbuild.patch
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
Requires:	avr-gcc avr-gcc-c++ avr-libc-doc avrdude


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
Requires:	avr-gcc avr-gcc-c++ avr-libc-doc avrdude


%description -n %{name}-doc
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains reference documentation.


%prep
%setup -q -n Arduino-%{version}
# The "extra" wifi components are licensed non-free and do not fall under the
# "firmware" execption.
rm -rf hardware/arduino/avr/firmwares/wifishield
rm -rf libraries/WiFi/extras
# As mentioned earlier, binary forms are removed here.
find -type d \( -name macosx -o -name windows \) -print0 | xargs -0 rm -rf
find -name '*.tgz' -delete
find -name '*.tar.gz' -delete
find -name '*.elf' -delete
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.so' -delete
find -name '*.hex' -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

echo -e "\n# By default, don't notify the user of a new upstream version." \
        "\n# https://bugzilla.redhat.com/show_bug.cgi?id=773519" \
        "\nupdate.check=false" \
    >> build/shared/lib/preferences.txt

build-jar-repository -p -s arduino-core/lib/ apache-commons-codec \
apache-commons-compress apache-commons-exec apache-commons-lang3 \
apache-commons-logging apache-commons-net bcpg bcprov jackson-core \
jackson-databind jackson-module-mrbean jmdns jsch jsemver jssc guava \
objectweb-asm jackson-annotations

build-jar-repository -p -s app/lib/ guava apache-commons-logging \
jakarta-commons-httpclient jsch apache-commons-lang3 jssc jsemver

touch app/test/cc/arduino/packages/contributions/library_index.json

%build
pushd build
ant
echo %{version} | ant dist
mv linux/%{name}*.tar.xz linux/%{name}-%{version}.tar.xz
tar -xf linux/%{name}-%{version}.tar.xz
popd

%install
cd build/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -a arduino $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a hardware lib libraries examples $RPM_BUILD_ROOT/%{_datadir}/%{name}/
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/*.jar
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/tools

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a ../../license.txt ../../README.md $RPM_BUILD_ROOT/%{_docdir}/%{name}/

# Requested upstream in http://github.com/arduino/Arduino/pull/4:
find $RPM_BUILD_ROOT -type f -iname *.jpg -or -iname *.java -or -iname *.pde -or -iname *.h -or -iname *.cpp -or -iname *.c -or -iname *.txt -or -iname makefile -or -iname key*.txt -or -iname pref*.txt | xargs chmod -x;

cp -a lib/arduino-core.jar lib/pde.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/

mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/dist
cp -a dist/package_index.json dist/package_index.json.sig \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/dist

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/boards.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/programmers.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/preferences.txt \
   $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
ln -s %{_sysconfdir}/%{name}/boards.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/boards.txt
ln -s %{_sysconfdir}/%{name}/programmers.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/programmers.txt
ln -s %{_sysconfdir}/%{name}/preferences.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/preferences.txt

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ../linux/dist/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages
cp -a ../linux/dist/mime.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages/%{name}.xml

for dir in ../shared/icons/*; do
    if [ -d $dir ]
    then
        size=`basename $dir`
        mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
        cp $dir/apps/%{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps/
    fi
done

install -D ../linux/dist/%{name}-add-groups $RPM_BUILD_ROOT%{_libexecdir}/%{name}-add-groups

mkdir -p $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions
cp -a ../linux/dist/cc.arduino.add-groups.policy $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cp -a ../linux/dist/appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
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
%{_datadir}/appdata/%{name}.appdata.xml

%files -n %{name}-doc
%{_docdir}/%{name}/

%files -n %{name}-core
%doc license.txt
%doc README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/boards.txt
%config(noreplace) %{_sysconfdir}/%{name}/programmers.txt
%config(noreplace) %{_sysconfdir}/%{name}/preferences.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/hardware/
%{_datadir}/%{name}/libraries/
%{_datadir}/%{name}/dist/
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/version.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_8jpp8
- new fc release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_6jpp8
- new version

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

