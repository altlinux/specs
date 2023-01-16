Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global antflags -Dno_arduino_builder=true -Dsystem_avr=true -Dlight_bundle=true

%global appstream_id cc.arduino.arduinoide

%global avr_version 1.8.2
%global ethernet_version 2.0.0
%global gsm_version 1.0.6
%global stepper_version 1.1.3
%global tft_version 1.0.6
%global wifi_version 1.2.7
%global firmata_version 2.5.8
%global bridge_version 1.7.0
%global robot_control_version 1.0.4
%global robot_motor_version 1.0.3
%global robotirremote_version 2.0.0
%global spacebrewyun_version 1.0.2
%global temboo_version 1.2.1
%global esplora_version 1.0.4
%global mouse_version 1.0.1
%global keyboard_version 1.0.2
%global sd_version 1.2.4
%global servo_version 1.1.6
%global liquidcrystal_version 1.0.7
%global adafruit_version 1.10.4

%global reference_version 1.6.6-3
%global wifi_firmware_updater_version 0.10.10

Name:           arduino
Epoch:          1
Version:        1.8.13
Release:        alt3_5jpp11
Summary:        An IDE for Arduino-compatible electronics prototyping platforms

License:        GPLv2+ and LGPLv2+ and CC-BY-SA
URL:            https://www.arduino.cc/
Source0:        https://github.com/arduino/Arduino/archive/%{version}/%{name}-%{version}.tar.gz

Source10:       https://downloads.arduino.cc/cores/avr-%{avr_version}.tar.bz2
Source11:       https://github.com/arduino-libraries/Ethernet/archive/%{ethernet_version}/Ethernet-%{ethernet_version}.zip
Source12:       https://github.com/arduino-libraries/GSM/archive/%{gsm_version}/GSM-%{gsm_version}.zip
Source13:       https://github.com/arduino-libraries/Stepper/archive/%{stepper_version}/Stepper-%{stepper_version}.zip
Source14:       https://github.com/arduino-libraries/TFT/archive/%{tft_version}/TFT-%{tft_version}.zip
Source15:       https://github.com/arduino-libraries/WiFi/archive/%{wifi_version}/WiFi-%{wifi_version}.zip
Source16:       https://github.com/firmata/arduino/archive/%{firmata_version}/Firmata-%{firmata_version}.zip
Source17:       https://github.com/arduino-libraries/Bridge/archive/%{bridge_version}/Bridge-%{bridge_version}.zip
Source18:       https://github.com/arduino-libraries/Robot_Control/archive/%{robot_control_version}/Robot_Control-%{robot_control_version}.zip
Source19:       https://github.com/arduino-libraries/Robot_Motor/archive/%{robot_motor_version}/Robot_Motor-%{robot_motor_version}.zip
Source20:       https://github.com/arduino-libraries/RobotIRremote/archive/%{robotirremote_version}/RobotIRremote-%{robotirremote_version}.zip
Source21:       https://github.com/arduino-libraries/SpacebrewYun/archive/%{spacebrewyun_version}/SpacebrewYun-%{spacebrewyun_version}.zip
Source22:       https://github.com/arduino-libraries/Temboo/archive/%{temboo_version}/Temboo-%{temboo_version}.zip
Source23:       https://github.com/arduino-libraries/Esplora/archive/%{esplora_version}/Esplora-%{esplora_version}.zip
Source24:       https://github.com/arduino-libraries/Mouse/archive/%{mouse_version}/Mouse-%{mouse_version}.zip
Source25:       https://github.com/arduino-libraries/Keyboard/archive/%{keyboard_version}/Keyboard-%{keyboard_version}.zip
Source26:       https://github.com/arduino-libraries/SD/archive/%{sd_version}/SD-%{sd_version}.zip
Source27:       https://github.com/arduino-libraries/Servo/archive/%{servo_version}/Servo-%{servo_version}.zip
Source28:       https://github.com/arduino-libraries/LiquidCrystal/archive/%{liquidcrystal_version}/LiquidCrystal-%{liquidcrystal_version}.zip
Source29:       https://github.com/Adafruit/Adafruit_CircuitPlayground/archive/%{adafruit_version}/Adafruit_Circuit_Playground-%{adafruit_version}.zip

Source50:       https://downloads.arduino.cc/reference-%{reference_version}.zip
Source51:       https://github.com/arduino-libraries/WiFi101-FirmwareUpdater-Plugin/releases/download/v%{wifi_firmware_updater_version}/WiFi101-Updater-ArduinoIDE-Plugin-%{wifi_firmware_updater_version}.zip

Patch0:         arduino-use-system-avrdude.patch
Patch1:         arduino-use-system-astyle.patch
Patch2:         arduino-use-system-libserialport.patch
Patch3:         arduino-drop-macosx.patch
Patch4:         arduino-wrapper.patch
Patch5:         arduino-add-to-groups.patch
Patch6:         arduino-fix-path-to-builder.patch
Patch7:         arduino-fix-fresh-rsyntaxtextarea.patch

BuildRequires:  ant
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  javapackages-tools

BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fifesoft:rsyntaxtextarea)
BuildRequires:  mvn(com.github.zafarkhaja:java-semver)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-net)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-all)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15)
BuildRequires:  mvn(org.jmdns:jmdns)
BuildRequires:  mvn(org.scream3r:jssc)

Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       javapackages-tools
Requires:       polkit

# Require arduino-builder, which is a go project and won't exist outside these arches
Requires:       %{name}-builder >= 1.3.25

BuildArch:      noarch
ExcludeArch:    ppc64le s390x
Source44: import.info
Patch33: arduino-1.8.5-use-system-listSerialsj.patch

%description
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains an IDE that can be used to develop and upload code
to the micro-controller.

%package        core
Group: Development/Java
Summary:        Files required for compiling code for Arduino-compatible micro-controllers

Requires:       %{name}-doc = %{epoch}:%{version}-%{release}
Requires:       %{name}-listSerialPortsC
Requires:       astyle libastyle
Requires:       avrdude
Requires:       avr-gcc
Requires:       avr-gcc-c++
Requires:       avr-libc
Requires:       java

Requires:       mvn(apache:commons-httpclient)
Requires:       mvn(com.fasterxml.jackson.core:jackson-annotations)
Requires:       mvn(com.fasterxml.jackson.core:jackson-core)
Requires:       mvn(com.fasterxml.jackson.core:jackson-databind)
Requires:       mvn(com.fifesoft:rsyntaxtextarea)
Requires:       mvn(com.github.zafarkhaja:java-semver)
Requires:       mvn(com.jcraft:jsch)
Requires:       mvn(commons-codec:commons-codec)
Requires:       mvn(commons-io:commons-io)
Requires:       mvn(org.apache.commons:commons-compress)
Requires:       mvn(org.apache.commons:commons-exec)
Requires:       mvn(org.apache.commons:commons-lang3)
Requires:       mvn(org.apache.commons:commons-logging)
Requires:       mvn(org.apache.commons:commons-net)
Requires:       mvn(org.apache.logging.log4j:log4j-api)
Requires:       mvn(org.apache.xmlgraphics:batik-all)
Requires:       mvn(org.apache.xmlgraphics:xmlgraphics-commons)
Requires:       mvn(org.bouncycastle:bcpg-jdk15)
Requires:       mvn(org.jmdns:jmdns)
Requires:       mvn(org.ow2.asm:asm)
Requires:       mvn(org.scream3r:jssc)
Requires:       mvn(org.slf4j:slf4j-api)
Requires:       mvn(xml-apis:xml-apis)

%description    core
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains the core files required to compile and upload
Arduino code.

%package        doc
Group: Development/Java
Summary:        Documentation for the Arduino micro-controller platform
BuildArch: noarch

%description    doc
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains reference documentation.

%package        devel
Group: Development/Java
Summary:        Devel package for %{name}

Requires:       %{name}-core

%description    devel
Devel package for %{name}.


%prep
%setup -q -n Arduino-%{version}


tar -xvf %{SOURCE10} -C hardware

# Need improve this moment...
# patch0 requires unpacked archive with hardware things
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

cp %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} build/
cp %{SOURCE50} %{SOURCE51} build/shared/

# Remove Windows and OSX specific code
find -type d \( -name macosx -o -name windows \) -print0 | xargs -0 rm -rf

# Drop binaries
find -name '*.elf' -delete
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.so' -delete

# Disable update check
echo -e "\n# By default, don't notify the user of a new upstream version." \
        "\n# https://bugzilla.redhat.com/show_bug.cgi?id=773519" \
        "\nupdate.check=false" >> build/shared/lib/preferences.txt

# Include requires jars to arduino-core/lib folder
build-jar-repository -p arduino-core/lib/ \
    apache-commons-codec \
    apache-commons-compress \
    apache-commons-exec \
    apache-commons-io \
    apache-commons-lang3 \
    apache-commons-logging \
    apache-commons-net \
    bcpg \
    bcprov \
    jackson-annotations \
    jackson-core \
    jackson-databind \
    jmdns \
    jsch \
    jsemver \
    jssc

# Include few libraries manually
ln -s /usr/share/java/log4j/log4j-api.jar arduino-core/lib/log4j-api.jar

# Include requires jars to app/lib folder
build-jar-repository -p app/lib/ \
    apache-commons-compress \
    apache-commons-lang3 \
    batik \
    jsch \
    jsemver \
    jssc \
    rsyntaxtextarea
    
# Include library manually
ln -s /usr/share/java/log4j/log4j-api.jar app/lib/log4j-api.jar
%patch33 -p1


%build
pushd build
echo %{version} | ant build %{antflags}
mkdir -p linux/work/hardware/arduino/
mv ../hardware/*/ linux/work/hardware/arduino/
popd


%install
pushd build

# Install wrapper
install -m 0755 -Dp linux/work/%{name} %{buildroot}%{_bindir}/%{name}

# Install desktop file
cp -p linux/dist/desktop.template linux/dist/%{appstream_id}.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications --set-icon=%{appstream_id} --set-key=Exec --set-value=%{name} linux/dist/%{appstream_id}.desktop

# Install app data
install -m 0644 -Dp linux/dist/appdata.xml %{buildroot}%{_datadir}/metainfo/%{appstream_id}.appdata.xml

# Install mime data
install -m 0644 -Dp linux/dist/mime.xml %{buildroot}%{_datadir}/mime/packages/%{appstream_id}.xml

# Install icons
for dir in shared/icons/*; do
    if [ -d $dir ]
    then
        size=`basename $dir`
        install -m 0644 -Dp $dir/apps/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{appstream_id}.png
    fi
done


# Install libs, examples, etc
mkdir -p                                    %{buildroot}%{_datadir}/%{name}
cp -ap linux/work/{examples,hardware,lib}   %{buildroot}%{_datadir}/%{name}/

rm -rf \
    %{buildroot}%{_datadir}/%{name}/lib/*.jar \
    %{buildroot}%{_datadir}/%{name}/lib/desktop.template \
    %{buildroot}%{_datadir}/%{name}/lib/version.txt \
    %{buildroot}%{_datadir}/%{name}/hardware/tools

cp -a linux/work/lib/{arduino-core.jar,pde.jar} %{buildroot}%{_datadir}/%{name}/lib/

install -m 0755 -Dp linux/dist/%{name}-add-groups %{buildroot}%{_libexecdir}/%{name}-add-groups
install -m 0644 -Dp linux/dist/cc.arduino.add-groups.policy %{buildroot}%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy

# Install configs
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
ln -s %{_datadir}/%{name}/hardware/%{name}/avr/boards.txt       %{buildroot}%{_sysconfdir}/%{name}/boards.txt
ln -s %{_datadir}/%{name}/hardware/%{name}/avr/programmers.txt  %{buildroot}%{_sysconfdir}/%{name}/programmers.txt
ln -s %{_datadir}/%{name}/lib/preferences.txt           %{buildroot}%{_sysconfdir}/%{name}/preferences.txt

popd
# unFedorize; ALTize
if grep 'dialout lock' %buildroot/%_bindir/arduino; then
   sed -i -e 's,dialout lock,uucp,' %buildroot/%_bindir/arduino
else
   echo "ALT-specific group hack is deprecated"
   exit 2
fi
sed -i 1s,/usr/bin/bash,/bin/bash, %buildroot{%_bindir/%name,%_libexecdir/arduino-add-groups}

# Create empty directory to prevent compiler error (ALT #42586).
mkdir -p %buildroot%_datadir/arduino/tools-builder

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# Disabled because nothing provides org.fest.swing.*
# # Include requires jars to app/lib folder
# build-jar-repository -p app/test-lib/ \
#     jackson-databind \
#     junit
# 
# pushd build
# ant test
# popd


%files core
%doc --no-dereference license.txt
%doc README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lib/
%dir %{_datadir}/arduino/tools-builder

%files doc
%{_datadir}/%{name}/examples/

%files devel
%{_datadir}/%{name}/hardware/

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}-add-groups
%{_datadir}/applications/%{appstream_id}.desktop
%{_datadir}/metainfo/%{appstream_id}.appdata.xml
%{_datadir}/mime/packages/%{appstream_id}.xml
%{_datadir}/icons/hicolor/*/apps/%{appstream_id}.png
%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy


%changelog
* Mon Jan 16 2023 Andrey Cherepanov <cas@altlinux.org> 1:1.8.13-alt3_5jpp11
- created empty directory to prevent compiler error (ALT #42586).

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 1:1.8.13-alt2_5jpp11
- fixed dependency on objectweb-asm 9

* Mon May 17 2021 Igor Vlasenko <viy@altlinux.org> 1:1.8.13-alt1_5jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt3_8jpp8
- new version

* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_8jpp8
- fixed avrdude path (closes: #37154)

* Fri Jul 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_7jpp8
- fc update & java 8 build

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_4jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_3jpp8
- java update

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_1jpp8
- fixed load of liblistSerialsj

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt1_1jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.6.6-alt1_1jpp8
- new version

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

