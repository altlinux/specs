Name: noXShmQuery
Version: 0.1
Release: alt1

Summary: Invoke executables with XShmQuery* functions disabled
License: GPLv2+
Group: Development/Other

%description
The noXShmQuery utility helps invoking executables with
XShmQueryExtension and XShmQueryVersion functions disabled.

%prep
%setup -cT
cat > %name << 'EOF'
#!/bin/sh -efu
LD_PRELOAD="${LD_PRELOAD-}${LD_PRELOAD:+:}%_libdir/%name.so" exec "$@"
EOF
cat > %name.c << 'EOF'
int XShmQueryExtension(void) { return 0; }
int XShmQueryVersion(void) { return 0; }
EOF

%build
gcc %optflags -shared -o %name.so %name.c

%install
mkdir -p %buildroot{%_bindir,%_libdir}
install -pm755 %name %buildroot%_bindir/
install -pm644 %name.so %buildroot%_libdir/

%files
%_bindir/%name
%_libdir/%name.so

%changelog
* Fri Aug 05 2016 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
