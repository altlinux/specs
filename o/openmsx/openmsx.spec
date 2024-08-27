Name: openmsx
Version: 19.1
Release: alt1.1
Summary: An emulator of the MSX home computer system	
Group: Emulators
License: GPL2
Url: https://openmsx.org/

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ make rpm-macros-make
BuildRequires: zlib-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libglew-devel
BuildRequires: libvorbis-devel libalsa-devel
BuildRequires: python3
BuildRequires: tcl-devel
BuildRequires: libtheora-devel
BuildRequires: libxml2-devel
BuildRequires: bzlib-devel libpng-devel libgtk+2-devel libssl-devel

ExcludeArch: armh

%description
An emulator of the MSX home computer system


%prep
%setup -n %name-%version


%build

cat > build/flavour-rpm.mk << EOF
# Opt flags.
CXXFLAGS+=%{optflags} -DNDEBUG
LINK_FLAGS+=%{__global_ldflags}
# Dont strip exe, let rpm do it and save debug info
OPENMSX_STRIP:=false
CATAPULT_STRIP:=false
EOF

cat > build/custom.mk << EOF
PYTHON:=python3
INSTALL_BASE:=%{_prefix}
VERSION_EXEC:=false
SYMLINK_FOR_BINARY:=false
INSTALL_CONTRIB:=false
INSTALL_SHARE_DIR=%{_datadir}/%{name}
INSTALL_DOC_DIR=%{_docdir}/%{name}
EOF

%configure
make  -j2 OPENMSX_FLAVOUR=rpm V=1

%install
mkdir -p %buildroot%prefix
%makeinstall_std PREFIX=%_prefix

%files
%doc doc/* README
%dir %_datadir/%name
%_bindir/%name
%_datadir/%name

%changelog
* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 19.1-alt1.1
- fix version

* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 19.1-alt1
- update to new version

* Sat Jun 24 2023 Artyom Bystrov <arbars@altlinux.org> 18-alt1.1
- Fix build with GCC13

* Sun Aug 7 2022 Artyom Bystrov <arbars@altlinux.org> 18-alt1
 - initial release
