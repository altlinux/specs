Name: sikuli-x
Version: 1.0
Release: alt6.rc3.1

Summary: GUI control scripting tool
License: MIT
Group: Development/Other
Url: http://sikuli.org/

Source0: %name-%version.tar
Source1: sikuli-ide.sh

Patch0: use-system-libs.patch
Patch1: use-system-loader.patch
Patch2: fix-find-libraries.patch
Patch3: no-opencv-surf-module.patch
Patch4: gcc-4.7.patch
Patch5: fix-deprecated-api.patch
Patch6: update-to-tesseract3.patch

BuildPreReq: rpm-build-java

BuildRequires: cmake gcc-c++ java-devel-default swig tesseract tesseract-devel tesseract-eng libopencv-devel libtiff-devel python-module-sphinx
BuildRequires: jython apache-commons-cli junit junit3 swing-layout json_simple swingx mockito jxgrabkey jgoodies-forms jgoodies-common macwidgets

Requires: sikuli-ide = %version-%release

%description
Sikuli mixes image recognition into jython scripting to automate
interactions with graphical user interfaces. You can programmatically
control a web page, a desktop application running on Windows/Linux/Mac
OS X, or even an iphone application running in an emulator.

%package -n sikuli-ide
Summary: GUI control scripting tool
License: MIT
Group: Development/Other

Requires: apache-commons-cli swing-layout json_simple junit3 macwidgets
Requires: jgoodies-forms >= 1.4 jgoodies-common >= 1.4
Requires: swingx >= 1.6.1

Requires: sikuli-script = %version-%release

BuildArch: noarch

%description -n sikuli-ide
%summary

This package contains the SikuliIDE program.

%package -n sikuli-script
Summary: GUI control scripting library
Requires: mockito jython jxgrabkey
License: MIT
Group: Development/Java

%description -n sikuli-script
%summary

This package contains the scripting library.

%prep
%setup -n %name-%version
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p2
sed -i -e 's,/usr/lib\([/":]\),%_libdir\1,g' `find -name 'CMakeLists.txt'` `find -name '*.cmake'`

%build
mkdir -p sikuli-script/build sikuli-ide/build

pushd sikuli-script/build
cmake ../
%make_build
popd

pushd sikuli-ide/build
cmake ../
subst 's/junit\.jar/junit3\.jar/' ../CMakeLists.txt
cmake ../
%make_build
popd

pushd docs
make html
popd

%install
# Install Java stuff
for jar in sikuli-*/target/*.jar; do
	install -D -m0644 $jar %buildroot%_datadir/java/${jar##*/}
done

# Install libs
for lib in sikuli-ide/target/linux/Sikuli-IDE/libs/*.so*; do
	install -D -m0644 $lib %buildroot%_libdir/sikuli/${lib##*/}
done

# Install the startup script
mkdir -p -m0755 %buildroot%_bindir
sed -e 's,^JARDIR=.*$,JARDIR=%_datadir/java,' \
    -e 's,^LIBPATH=.*$,LIBPATH=%_libdir/sikuli:%_libdir/java,' \
    %SOURCE1 >%buildroot%_bindir/sikuli
chmod 0755 %buildroot%_bindir/sikuli

%files -n sikuli-ide
%doc docs/README docs/build/html
%_datadir/java/sikuli-ide.jar
%_bindir/sikuli

%files -n sikuli-script
%_libdir/sikuli
%_datadir/java/sikuli-script.jar

%changelog
* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt6.rc3.1
- NMU: updated jar locations

* Tue Jun 23 2015 Sergey V Turchin <zerg@altlinux.org> 1.0-alt5.rc3.1
- Rebuild with gcc5

* Sat Dec 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.0-alt5.rc3
- Specified required junit version.

* Sat Dec 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.0-alt4.rc3
- Revision up for p7 rebuild.

* Thu Mar 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.0-alt3.rc3.1
- NMU: rebuild with libopencv-2.4.8.1;

* Wed Feb 20 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3.rc3
- Fix/improve the startup script.
- Extract the sikuli-script from the sikuli-ide (main) package.
- Use system jars and libs.
- Fix file layout.
- Fix/improve the system loader patch.
- Fix the init method call syntax (patch).
- Remove unused (?) code with dependency on the missing (nonfree) opencv
  SURF module (patch, thx pini@debian.org).
- Fix library path and names (patch)
- Merge-in the Tesseract 3 version of Sikuli (sikuli/feature/tesseract3).

* Mon Mar 21 2011 Dmitry Derjavin <dd@altlinux.org> 1.0-alt2.rc2
- using system libraries

* Thu Mar 17 2011 Dmitry Derjavin <dd@altlinux.org> 1.0-alt1.rc2
- initial build

