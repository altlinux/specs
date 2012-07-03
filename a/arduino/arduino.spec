BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: gcc-c++
Name:		arduino
Version:	0022
Release:	alt1_5jpp6
Summary:	An IDE for Arduino-compatible electronics prototyping platforms
Group:		Development/Java
License:	GPLv2+ and LGPLv2+ and CC-BY-SA
URL:		http://www.arduino.cc/

# There are lots of binaries in the "source" tarball.  Remove them with:
# curl -L http://arduino.googlecode.com/files/arduino-0022-src.tar.gz | tar -xzvf - && rm -r arduino-0022/build/linux/dist/tools/* && find arduino-0022 \( -type d \( -name macosx -o -name windows \) -o -type f \( -iname '*.jar' -or -iname '*.tgz' -or -iname '*.so' \) \) -print0 | xargs -0 rm -rf && tar -cjf arduino-0022.tar.bz2 arduino-0022
# See also http://code.google.com/p/arduino/issues/detail?id=193
Source0:	%{name}-%{version}.tar.bz2

BuildArch:	noarch

# Use unbundled libs:
Patch0:		arduino-script.patch
Patch2:		arduino-use-system-avrdude.patch
# Requested upstream in http://github.com/arduino/Arduino/pull/5:
Patch3:		arduino-use-system-rxtx.patch

# Requested upstream in http://github.com/arduino/Arduino/pull/6:
Patch4:		arduino-icons-etc.patch

# Shouldn't be necessary once
# https://code.google.com/p/arduino/issues/detail?id=106 has been fixed:
Patch5:		arduino-boards-txt.patch

Patch6:		arduino-add-to-groups.patch

BuildRequires:	jpackage-utils ant ant-apache-regexp desktop-file-utils ecj jna rxtx git
Requires:	%{name}-core = %{version}-%{release} %{name}-doc = %{version}-%{release}
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
%patch2
%patch3 -p1

# "git apply" fails silently if pwd is git-controlled.
pwd=`pwd`
cd /
git apply --directory=$pwd %{PATCH4}
cd $pwd

%patch5
build-jar-repository -p -s app/lib/ ecj jna RXTXcomm


%build
cd core/methods
ant
cd ..
ant
cd ../build
ant dist < /dev/null
tar -xf linux/%{name}-%{version}.tgz


%install
cd build/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -a arduino $RPM_BUILD_ROOT/%{_bindir}/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a hardware lib libraries examples $RPM_BUILD_ROOT/%{_datadir}/%{name}/
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/lib/*.jar
rm -r $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/tools

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}
cp -a reference $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}/
ln -s %{_defaultdocdir}/%{name}-%{version}/reference $RPM_BUILD_ROOT/%{_datadir}/%{name}/reference

# Requested upstream in http://github.com/arduino/Arduino/pull/4:
find $RPM_BUILD_ROOT -type f -iname *.jpg -or -iname *.java -or -iname *.pde -or -iname *.h -or -iname *.cpp -or -iname *.c -or -iname *.txt -or -iname makefile -or -iname key*.txt -or -iname pref*.txt | xargs chmod -x;

cp -a lib/core.jar lib/pde.jar $RPM_BUILD_ROOT/%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/boards.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/programmers.txt \
   $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/
ln -s %{_sysconfdir}/%{name}/boards.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/boards.txt
ln -s %{_sysconfdir}/%{name}/programmers.txt \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/%{name}/programmers.txt

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp -p ../linux/%{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ../linux/%{name}.desktop

for dir in ../linux/icons/*; do
    size=`basename $dir`
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/$size/apps
    cp $dir/%{name}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/$size/apps/
done

mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}
cp -a ../linux/%{name}-add-groups $RPM_BUILD_ROOT/%{_libexecdir}/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/polkit-1/actions
cp -a ../linux/cc.arduino.add-groups.policy $RPM_BUILD_ROOT/%{_datadir}/polkit-1/actions

%files
%{_bindir}/*
%{_datadir}/%{name}/*.jar
%{_datadir}/%{name}/lib/
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy
%{_libexecdir}/%{name}-add-groups
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}/reference


%files -n %{name}-core
%doc license.txt readme.txt todo.txt
%config(noreplace) %{_sysconfdir}/%{name}/boards.txt
%config(noreplace) %{_sysconfdir}/%{name}/programmers.txt
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/hardware/
%{_datadir}/%{name}/libraries/


%files -n %{name}-doc
%{_defaultdocdir}/%{name}-%{version}/


%changelog
* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_5jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_4jpp6
- update to new release by jppimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_3jpp6
- import by jppimport

