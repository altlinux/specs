%define _unpackaged_files_terminate_build 1

%define sover 1
%define libname libespeak-ng%sover

Name: espeak-ng
Version: 1.52.0
Release: alt2

Summary: eSpeak NG Text-to-Speech

License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/espeak-ng/espeak-ng

Source: %name-%version.tar

# Debian patches
Patch0: klatt-garbage
Patch1: libsonic-bigendian
Patch2: bufsize
Patch3: fix-cancel
Patch4: privacy
Patch5: x
Patch6: CI
Patch7: nocard
Patch8: clang-target
Patch9: fuzz-link
Patch10: th_dict
Patch11: compile-reproducibility
Patch12: espeak-stdin
Patch13: piper

BuildRequires: gcc-c++
BuildRequires: ronn
BuildRequires: kramdown
BuildRequires: pcaudiolib-devel

%description
The eSpeak NG is a compact open source software text-to-speech synthesizer for 
Linux, Windows, Android and other operating systems. It supports 
more than 100 languages and accents. It is based on the eSpeak engine
created by Jonathan Duddington.

eSpeak NG uses a "formant synthesis" method. This allows many languages to be
provided in a small size. The speech is clear, and can be used at high speeds,
but is not as natural or smooth as larger synthesizers which are based on human
speech recordings. It also supports Klatt formant synthesis, and the ability
to use MBROLA as backend speech synthesizer.

%package espeak
Summary: Multi-lingual software speech synthesizer
Group: Sound
BuildArch: noarch
Provides: espeak = %EVR
Obsoletes: espeak < %EVR

%description espeak
This package contains compatibility links that makes it a drop-in replacement
 for the espeak package.  Installing this package thus allows one to make
 applications calling the /usr/bin/espeak program use eSpeak NG without any
 modification or rebuild.

%package -n %libname
Group: System/Libraries
Summary: Lib files for espeak-ng
Requires: %name-data = %EVR
Provides: libespeak-ng = %EVR
Obsoletes: libespeak-ng < %EVR

%description -n %libname
Lib files for espeak-ng

%package -n lib%name-libespeak%sover
Group: System/Libraries
Summary: Links fore libespeak
Provides: libespeak = %EVR
Obsoletes: libespeak < %EVR
Provides: libespeak%sover = %EVR
Obsoletes: libespeak%sover < %EVR

%description -n lib%name-libespeak%sover
This package contains compatibility links that makes it a drop-in replacement
 for the libespeak1 package.  Installing this package thus allows one to make
 applications linked against libespeak1 use eSpeak NG without any modification
 or rebuild.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for espeak-ng
Provides: espeak-ng-devel = %EVR
Obsoletes: espeak-ng-devel < %EVR

%description -n lib%name-devel
Development files for eSpeak NG, a software speech synthesizer.

%package -n lib%name-libespeak-devel
Group: Development/C++
Summary: Development files for espeak
Provides: libespeak-devel = %EVR
Obsoletes: libespeak-devel < %EVR
Provides: espeak-devel = %EVR
Obsoletes: espeak-devel < %EVR

%description -n lib%name-libespeak-devel
This package contains compatibility links that makes it a drop-in replacement
 for the libespeak-dev package.  Building against this package thus allows one
 to migrate to using eSpeak NG without any source code change.

%package vim
Group: Sound
Summary: Vim syntax highlighting for espeak-ng data files
BuildArch: noarch
Requires: %name = %EVR

%description vim
%summary

%package doc
Summary: Doc files fore %name
Group: Documentation
BuildArch: noarch

%description doc
%summary

%package data
Summary: Necessary synthesizer data files fore %name
Group: Other
BuildArch: noarch

%description data
This package contains necessary synthesizer data files needed
 for the %name program and the shared library.

%prep
%setup
# Remove unused files to make sure we've got the License tag right
rm -rf src/include/compat/endian.h src/compat/getopt.c android/
%autopatch -p1

%build
./autogen.sh
%configure --with-extdict-ru=yes --with-extdict-cmn=yes --with-extdict-yue=yes
%make_build src/espeak-ng src/speak-ng
%make
LC_ALL=C.UTF-8 %make docs

%install
%makeinstall_std PREFIX=%prefix
rm -v %buildroot%_libdir/*.{a,la}

# Move Vim files
mv %buildroot%_datadir/vim/addons %buildroot%_datadir/vim/vimfiles
rm -vr %buildroot%_datadir/vim/registry

ln -s libespeak-ng.so %buildroot%_libdir/libespeak.so
ln -s libespeak-ng.so.%sover %buildroot%_libdir/libespeak.so.%sover
ln -s espeak-ng.pc %buildroot%_pkgconfigdir/espeak.pc

%check
ESPEAK_DATA_PATH=`pwd` LD_LIBRARY_PATH=src:${LD_LIBRARY_PATH} src/espeak-ng ...

%files
%_bindir/speak-ng
%_bindir/espeak-ng
%_man1dir/speak-ng.1.xz
%_man1dir/espeak-ng.1.xz

%files espeak
%_bindir/speak
%_bindir/espeak

%files doc
%doc COPYING COPYING.* README *.md *.html ChangeLog.md AUTHORS INSTALL NEWS docs

%files data
%_datadir/espeak-ng-data

%files -n %libname
%_libdir/libespeak-ng.so.%sover
%_libdir/libespeak-ng.so.%sover.*

%files -n lib%name-libespeak%sover
%_libdir/libespeak.so.%sover

%files -n lib%name-devel
%_includedir/espeak-ng
%_libdir/libespeak-ng.so
%_pkgconfigdir/espeak-ng.pc

%files -n lib%name-libespeak-devel
%_includedir/espeak
%_libdir/libespeak.so
%_pkgconfigdir/espeak.pc

%files vim
%_datadir/vim/vimfiles/ftdetect/espeakfiletype.vim
%_datadir/vim/vimfiles/syntax/espeaklist.vim
%_datadir/vim/vimfiles/syntax/espeakrules.vim

%changelog
* Fri Jan 16 2026 Artem Semenov <savoptik@altlinux.org> 1.52.0-alt2
- Created compatibility package fore libespeak-devel
- Created compatibility package fore libespeak
- Dicts files moved to data package
- Espeak links moved to subpackage
- Updated description
- Builded doc package

* Tue Apr 15 2025 Artem Semenov <savoptik@altlinux.org> 1.52.0-alt1
- New version 1.52.0

* Tue Jun 11 2024 Artem Semenov <savoptik@altlinux.org> 1.51.1-alt4
- Fixed symlink espeak to espeak-ng

* Mon May 27 2024 Artem Semenov <savoptik@altlinux.org> 1.51.1-alt3
- The libespeak and libespeak-devel package has been replaced

* Mon May 27 2024 Artem Semenov <savoptik@altlinux.org> 1.51.1-alt2
- The espeak package has been replaced (ALT bug: 50440)

* Tue Mar 19 2024 Artem Semenov <savoptik@altlinux.org> 1.51.1-alt1
- Initial build for ALT Sisyphus (ALT bug: 49726)
  + (fixes: CVE-2023-49990 CVE-2023-49991 CVE-2023-49992 CVE-2023-49993 CVE-2023-49994)
