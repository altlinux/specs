Name: mbuffer
Version: 20220418
Release: alt1
Summary: Measuring Buffer is an enhanced version of buffer

Group: System/Base
License: GPLv3+
Url: http://www.maier-komor.de/mbuffer.html
Source0: http://www.maier-komor.de/software/mbuffer/mbuffer-%version.tar.gz

BuildRequires: mt-st, libmhash-devel

%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
%setup

%build
#autoconf
# suppress detection of MD5_Init functions if openssl-devel
# is available on build system, let only mhash_init be
# detected if the md5 hash feature is enabled
export ac_cv_search_MD5_Init=no
%ifarch x86_64
CFLAGS="%optflags -m64"; export CFLAGS
%endif
%configure
%make_build

%install
make install DESTDIR=%buildroot INSTALL="install -p"

%files
%doc AUTHORS ChangeLog LICENSE NEWS README
%config(noreplace) %_sysconfdir/%name.rc
%_man1dir/mbuffer.1*
%_bindir/%name

%changelog
* Thu Dec 15 2022 L.A. Kostis <lakostis@altlinux.ru> 20220418-alt1
- Updated to 20220418.

* Sun Mar 27 2022 L.A. Kostis <lakostis@altlinux.ru> 20211018-alt1
- Updated to 20211018.

* Tue Feb 23 2021 L.A. Kostis <lakostis@altlinux.ru> 20210209-alt1
- Updated to 20210209.
- Added config.

* Wed Oct 07 2015 L.A. Kostis <lakostis@altlinux.ru> 20150412-alt1
- Initial build based on Fedora package.
