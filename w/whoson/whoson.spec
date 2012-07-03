%def_disable static

Name: whoson
Version: 2.05
Release: alt2.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Protocol for Keeping Track of Dynamically Allocated IP
License: Public Domain
Group: Networking/Other

URL: http://whoson.sf.net/
Source0: http://download.sf.net/whoson/whoson-%version.tar.gz
Source1: whosond.init
Source2: whoson.conf

Requires: lib%name = %version-%release

# Automatically added by buildreq on Sun Oct 16 2011
BuildRequires: chrpath groff-base

%description
Simple method for Internet server programs to know if a particular (dynamically
allocated) IP address is currently allocated to a known (trusted) user and,
optionally, the identity of the said user.

%package server
Summary: Whoson server binary and scripts
Group: Networking/Other
Requires: %name = %version-%release

%description server
Whoson server binary and scripts

%package -n lib%name
Summary: Whoson library
Group: Development/C

%description -n lib%name
This is whoson library package.

%package -n lib%name-devel
Summary: Header files and development documentation for whoson
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is whoson development package. It includes files and development
documentation for whoson.

%package -n lib%name-devel-static
Summary: Static libraries for whoson
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
You should install the lib%name-devel-static package if you would like to
develop statically linked whoson applications.

%prep
%setup

%build
%configure %{subst_enable static}
# Parallel make broken in whoson 2.03 :(
%make

# Build with disabled static will insert rpath in whoson binary. Instead of
# patching build system we simply delete rpath from built executable.
chrpath -d whoson
chrpath -d .libs/whosond

%install
install -d %buildroot{%_initdir,/var/lib/whosond}

%make_install DESTDIR=%buildroot install
install -m0755 %SOURCE1 %buildroot%_initdir/whosond
install -m0644 %SOURCE2 %buildroot%_sysconfdir/

for i in wso_login wso_logout wso_query wso_version; do
	rm -f %buildroot%_man3dir/$i.3
	echo ".so whoson.3" > %buildroot%_man3dir/$i.3
done

%post server
%post_service whosond

%preun server
%preun_service whosond

%files
%_sbindir/whoson
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/whoson.conf
%_man5dir/*
%_man8dir/whoson.*

%files server
%_sbindir/whosond
%_initdir/whosond
%dir /var/lib/whosond
%_man8dir/whosond.*

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*
%_man3dir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif

%changelog
* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt2.1
- fixed circular dependencies

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt2
- rebuilt for debuginfo and soname set-versioning

* Sat Jul 11 2009 Victor Forsyuk <force@altlinux.org> 2.05-alt1
- 2.05

* Thu Jan 08 2009 Victor Forsyuk <force@altlinux.org> 2.04-alt1
- 2.04
- Remove obsolete ldconfig calls.

* Thu May 13 2004 Victor Forsyuk <force@altlinux.ru> 2.03-alt2
- libwhoson-devel depends on libwhoson package, not whoson.

* Wed Dec 31 2003 Victor Forsyuk <force@altlinux.ru> 2.03-alt1
- New version.
- Removed *.la files.
- Do not build devel-static subpackage by default.

* Fri May 23 2003 Victor Forsyuk <force@altlinux.ru> 2.02a-alt1
- Rewritten start/stop script to new rc scheme.

* Tue Jan 14 2003 Victor Forsyuk <force@altlinux.ru> 2.02a-alt0
- Initial build for Sisyphus.
