Name: filterXQueryExtension
Version: 0.1
Release: alt1

Summary: Invoke executables with XQueryExtension function filtered
License: GPLv2+
Group: Development/Other
Vcs: git://git.altlinux.org/gears/f/%name.git
Source: %name.c

%description
The filterXQueryExtension utility helps invoking executables with
XShmQueryExtension function filtered.

%prep
%setup -cT
cat > %name << 'EOF'
#!/bin/sh -efu
LD_PRELOAD="${LD_PRELOAD-}${LD_PRELOAD:+:}%_libdir/%name.so" exec "$@"
EOF

%build
gcc %optflags %optflags_shared -W -Werror -shared %_sourcedir/%name.c -ldl -o %name.so

%install
mkdir -p %buildroot{%_bindir,%_libdir}
install -pm755 %name %buildroot%_bindir/
install -pm644 %name.so %buildroot%_libdir/

%files
%_bindir/%name
%_libdir/%name.so

%changelog
* Sun Dec 29 2019 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
