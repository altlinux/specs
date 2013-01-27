%define __cc musl-gcc

%define _libexecdir %_exec_prefix/libexec

%define bname busybox
Name: %bname-hasher
Version: 1.21.0
Release: alt1
Summary: %bname's static utils for hasher
License: GPLv2
Group: System/Kernel and hardware
URL: http://%bname.net
AutoReq: no

BuildRequires: %bname-source = %version
# for cpio
BuildRequires: %bname-source >= %version-alt1
%if "%__cc" == "musl-gcc"
BuildRequires: musl-devel
%else
BuildRequires: glibc-devel-static
%endif
# due -flto flag
BuildRequires: gcc >= 4.6 binutils >= 2.22

%description
This package contains %bname's static utils for hasher:
  - sh/ash
  - cpio
  - find


%prep
%setup -cT -n %name-%version
tar -x --strip-components 1 -f %_usrsrc/%bname-%version.tar*
#echo "CFLAGS_ash.o += -fno-lto" >> shell/Kbuild.src


%build
config_enable() {
local e
while [ -n "$1" ]; do
	e="$e"'/^#[[:blank:]]*CONFIG_'$1'[[:blank:]]/s|^.*$|CONFIG_'$1'=y|;'
	shift
done
sed -i "$e" .config
}

config_disable() {
local e
while [ -n "$1" ]; do
	e="$e"'/^CONFIG_'$1'=/s|^.*$|# CONFIG_'$1' is not set|;'
	shift
done
sed -i "$e" .config
}

config_param() {
local e
while [ -n "$1" ]; do
	{ echo "$2" | grep -q '^[0-9][0-9]*$'; } &&
		e="$e"'/^CONFIG_'$1'=/s|^.*$|CONFIG_'$1=$2'|;' ||
		e="$e"'/^CONFIG_'$1'=/s|^.*$|CONFIG_'$1'="'$2'"|;'
	shift 2
done
sed -i "$e" .config
}

make allnoconfig

config_disable \
	FEATURE_SH_IS_NONE
config_enable \
	PLATFORM_LINUX \
	STATIC \
	LFS \
	INSTALL_NO_USR \
	SHOW_USAGE \
	FEATURE_VERBOSE_USAGE \
	LONG_OPTS \
	CPIO \
	FEATURE_CPIO_O \
	FIND \
	FEATURE_FIND_NOT \
	FEATURE_FIND_DEPTH \
	FEATURE_FIND_DELETE \
	FEATURE_FIND_PATH \
	ASH \
	ASH_BASH_COMPAT \
	ASH_BUILTIN_ECHO \
	ASH_BUILTIN_PRINTF \
	ASH_BUILTIN_TEST \
	FEATURE_BASH_IS_NONE \
	SH_MATH_SUPPORT \
	FEATURE_SH_IS_ASH \
	FEATURE_SH_EXTRA_QUIET

config_param \
	PREFIX %_libexecdir/hasher \
	GZIP_FAST 2 \
	EXTRA_CFLAGS -flto \
	EXTRA_LDFLAGS -flto

make oldconfig

%make_build %{?__cc:CC="%__cc"} %bname


%install
install -pD -m 0755 %bname %buildroot%_libexecdir/hasher/%bname


%files
%_libexecdir/hasher


%changelog
* Sun Jan 27 2013 Led <led@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Sat Nov 17 2012 Led <led@altlinux.ru> 1.20.2-alt1
- initial build
