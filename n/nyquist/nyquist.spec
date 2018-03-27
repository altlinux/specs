Name: nyquist
Version: 3.12
Release: alt1

Summary: Sound synthesis and composition language with a Lisp syntax
Group: Sound
License: BSD
Url: http://www-2.cs.cmu.edu/~music/music.software.html

Source: http://download.sourceforge.net/%name/nyqsrc312.zip
Source1: %name-Makefile
Patch: nyquist-3.12-alt-cmake.patch

BuildRequires: unzip cmake gcc-c++ libalsa-devel liblo-devel libportaudio2-devel
BuildRequires: libsndfile-devel libogg-devel libflac-devel libvorbis-devel
BuildRequires: /proc java-devel
BuildRequires: dos2unix

%description
Nyquist is a language for sound synthesis and music composition. Unlike
score languages that tend to deal only with events, or signal processing
languages that tend to deal only with signals and synthesis, Nyquist
handles both in a single integrated system. Nyquist is also flexible and
easy to use because it is based on an interactive Lisp interpreter.

%prep
%setup -n nyquist
%patch
cp %SOURCE1 ./Makefile

# remove cvs cruft
find -name CVS | xargs rm -fr
# add opt flags
sed -i "s|^CFLAGS =|CFLAGS = $RPM_OPT_FLAGS |" misc/Makefile
# remove dos paths that cause warnings
sed -i 's|(setdir ".:.*")||' runtime/fileio.lsp
# fix some permission
find -name "*.lsp" | xargs chmod 0644
sed -i 's|"./ny"|"ny"|' jnyqide/NyquistThread.java
# change end-of-line
find -name "*.htm*" \
    -or -name "*.lsp" \
    -or -name "*.txt" \
    -or -name "*.ny" \
    -or -name "*.dat" -exec dos2unix -q '{}' \;

%build
%cmake_insource -DUSE_SOURCE_LIBS=OFF
%make_build
rm -f runtime/system.lsp
#%make_build OPT="$RPM_OPT_FLAGS" -f Makefile

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/nyquist
mkdir -p %buildroot%_datadir/nyquist/java
mkdir -p %buildroot%_libexecdir

cp -pr runtime %buildroot%_datadir/nyquist
cp -pr lib %buildroot%_datadir/nyquist
cp -pr demos %buildroot%_datadir/nyquist
cp -p ny %buildroot%_libexecdir
cp -p jnyqide/jNyqIDE.jar %buildroot%_datadir/nyquist/java

cat > %buildroot%_bindir/ny <<EOF
#!/bin/sh
export XLISPPATH=%_datadir/nyquist/runtime:%_datadir/nyquist/lib
exec %_libexecdir/ny \$*
EOF
chmod 0755 %buildroot%_bindir/ny

cat > %buildroot%_bindir/jny <<EOF
#!/bin/sh
export XLISPPATH=%_datadir/nyquist/runtime:%_datadir/nyquist/lib
exec java -jar %_datadir/nyquist/java/jNyqIDE.jar \$*
EOF
chmod 0755 %buildroot%_bindir/jny

%files
%_bindir/ny
%_bindir/jny
%_libexecdir/ny
%_datadir/nyquist
%doc Readme.txt license.txt advantages.txt files.txt todo.txt
%doc doc

%changelog
* Tue Mar 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.12-alt1
- 3.12 (build with fixed cmake stuff)

* Tue Jul 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.09-alt1
- 3.09

* Sat Dec 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.08-alt1
- first build for Susiphus (based on fc spec)


