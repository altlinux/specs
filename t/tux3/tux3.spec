Name: tux3
Version: 0.0
Release: alt2
Summary: Tux3 versioning filesystem
License: GPLv3
Group: System/Kernel and hardware
URL: http://tux3.org
Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libfuse-devel >= 2.6

%description
Tux3 versioning filesystem.


%package utils
Summary: Utils of Tux3 versioning filesystem
Group: System/Kernel and hardware
Provides: %name-tools = %version-%release

%description utils
Utils of Tux3 versioning filesystem.


%package -n fuse-%name
Summary: FUSE variant of Tux3 versioning filesystem
Group: System/Kernel and hardware
Provides: %{name}fuse = %version-%release

%description -n fuse-%name
FUSE variant of Tux3 versioning filesystem.


%package doc
Summary: Tux3 versioning filesystem documentation
Group: Documentation
BuildArch: noarch

%description doc
Tux3 versioning filesystem documentation.


%prep
%setup -q
%patch -p1


%build
export CFLAGS="%optflags"
sed -i 's|\-Werror$||' user/Makefile
%make_build -C user TEST_LIB_OBJS= tux3{,fuse}
cat > tux3.sh <<__EOF__
#!/bin/sh
exec %_sbindir/tux3 \$(basename "\$0" .tux3) "\$@"
__EOF__


%install
install -d -m 0755 %buildroot{%_sbindir,%_bindir,%_docdir/%name-%version}
install -p -m 0755 user/tux3 tux3.sh %buildroot%_sbindir/
install -p -m 0755 user/tux3fuse %buildroot%_bindir/
install -p -m 0644 doc/* %buildroot%_docdir/%name-%version/
for i in dump fsck mkfs; do
	ln -s tux3.sh %buildroot%_sbindir/$i.tux3
done


%files utils
%_sbindir/*


%files -n fuse-%name
%_bindir/*


%files doc
%doc %_docdir/%name-%version


%changelog
* Mon Jul 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0-alt2
- Fixed build with gcc-6

* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.1
- Disabled -Werror flag

* Sun Apr 13 2014 Led <led@altlinux.ru> 0.0-alt1
- initial build
