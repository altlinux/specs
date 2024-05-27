%define _unpackaged_files_terminate_build 1

Name: espeak-ng
Version: 1.51.1
Release: alt2

Summary: eSpeak NG Text-to-Speech

License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/espeak-ng/espeak-ng
Requires: lib%name
Provides: espeak = %version-%release
Obsoletes: espeak < %version-%release

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkg-config
BuildRequires: gem-ronn-ng
BuildRequires: gem-kramdown
BuildRequires: pcaudiolib-devel

# Backported from:
# https://github.com/espeak-ng/espeak-ng/commit/58f1e0b6a4e6aa55621c6f01118994d01fd6f68c
Patch: %name-%version-CVE-2023-49990-4.patch

%description
The eSpeak NG (Next Generation) Text-to-Speech program is an open source speech
synthesizer that supports over 70 languages. It is based on the eSpeak engine
created by Jonathan Duddington. It uses spectral formant synthesis by default
which sounds robotic, but can be configured to use Klatt formant synthesis
or MBROLA to give it a more natural sound.

%package -n lib%name
Group: Sound
Summary: Lib files for espeak-ng
Requires: %name = %EVR

%description -n lib%name
Lib files for espeak-ng

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for espeak-ng
Requires: %name = %EVR

%description -n lib%name-devel
Development files for eSpeak NG, a software speech synthesizer.

%package vim
Group: Sound
Summary: Vim syntax highlighting for espeak-ng data files
BuildArch: noarch
Requires: %name = %EVR

%description vim
%summary

%prep
%setup
%patch0 -p1
# Remove unused files to make sure we've got the License tag right
rm -rf src/include/compat/endian.h src/compat/getopt.c android/

%build
./autogen.sh
%configure
%make_build src/espeak-ng src/speak-ng
%make

%install
%makeinstall_std PREFIX=%prefix
rm -vf %buildroot%_libdir/libespeak-ng-test.so*
rm -vf %buildroot%_libdir/*.{a,la}

# Move Vim files
mv %buildroot%_datadir/vim/addons %buildroot%_datadir/vim/vimfiles
rm -vr %buildroot%_datadir/vim/registry

%files
%doc COPYING COPYING.* README.md CHANGELOG.md
%_bindir/speak-ng
%_bindir/espeak-ng
%_bindir/speak
%_bindir/espeak
%_datadir/espeak-ng-data
%_man1dir/speak-ng.1.xz
%_man1dir/espeak-ng.1.xz

%files -n lib%name
%_libdir/libespeak-ng.so.1
%_libdir/libespeak-ng.so.1.*

%files -n lib%name-devel
%_pkgconfigdir/espeak-ng.pc
%_libdir/libespeak-ng.so
%_includedir/espeak-ng
%_includedir/espeak

%files vim
%_datadir/vim/vimfiles/ftdetect/espeakfiletype.vim
%_datadir/vim/vimfiles/syntax/espeaklist.vim
%_datadir/vim/vimfiles/syntax/espeakrules.vim

%changelog
* Mon May 27 2024 Artem Semenov <savoptik@altlinux.org> 1.51.1-alt2
- The espeak package has been replaced (ALT bug: 50440)

* Tue Mar 19 2024 Artem Semenov <savoptik@altlinux.org> 1.51.1-alt1
- Initial build for ALT Sisyphus (ALT bug: 49726)
  + (fixes: CVE-2023-49990 CVE-2023-49991 CVE-2023-49992 CVE-2023-49993 CVE-2023-49994)
  
