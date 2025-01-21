%define _libexecdir %_usr/libexec

Name: glimpse
Version: 4.12.6
Release: alt1
Summary: Powerful file indexing and query system

License: ISC
Group: Text tools
URL: https://github.com/gvelez17/glimpse
Source: %name-%version.tar

BuildRequires:  flex

Requires:       agrep

%description
Glimpse is a very powerful indexing and query system that allows you to
search through all your files very quickly.  It can be used by
individuals for their personal file systems as well as by organizations
for large data collections.


%prep
%setup


%build
autoconf
%configure
sed -i '/^DEFS/s/$/ -Wno-error=return-mismatch -Wno-error=implicit-int -Wno-error=implicit-function-declaration/' agrep/Makefile compress/Makefile dynfilters/Makefile index/Makefile libtemplate/util/Makefile Makefile

# Parallel make breaks it
make DEBUGFLAGS="" OTHERLIBS=""


%install
make install prefix="%buildroot%_prefix" exec_prefix="%buildroot%_prefix" manprefix="%buildroot%_mandir"

# Move undocumented commands to libexec
mkdir -p %buildroot%_libexecdir/%name
mv %buildroot%_bindir/*cast %buildroot%_bindir/tbuild %buildroot%_bindir/wgconvert %buildroot%_libexecdir/%name

# Drop agrep, as we have another provider for it
rm -v %buildroot%_bindir/agrep %buildroot%_man1dir/agrep.1*


%files
%doc README KNOWN_BUGS ChangeLog CHANGES
%_bindir/glimpse*
%_man1dir/glimpse*
%_libexecdir/glimpse/


%changelog
* Mon Jan 20 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.12.6-alt1
- Initial build for ALT.
