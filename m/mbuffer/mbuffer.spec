Name: mbuffer
Version: 20230301
Release: alt1
Summary: Measuring Buffer is an enhanced version of buffer

Group: System/Base
License: GPLv3+
Url: http://www.maier-komor.de/mbuffer.html
Source0: http://www.maier-komor.de/software/mbuffer/mbuffer-%version.tar.gz

BuildRequires: mt-st, libssl-devel

%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
%setup

%build
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
* Mon Mar 06 2023 L.A. Kostis <lakostis@altlinux.ru> 20230301-alt1
- Updated to 20230301.
- Fix md5 detection when using openssl.

* Thu Dec 15 2022 L.A. Kostis <lakostis@altlinux.ru> 20220418-alt2
- Use libssl instead of mhash library.

* Thu Dec 15 2022 L.A. Kostis <lakostis@altlinux.ru> 20220418-alt1
- Updated to 20220418.

* Sun Mar 27 2022 L.A. Kostis <lakostis@altlinux.ru> 20211018-alt1
- Updated to 20211018.

* Tue Feb 23 2021 L.A. Kostis <lakostis@altlinux.ru> 20210209-alt1
- Updated to 20210209.
- Added config.

* Wed Oct 07 2015 L.A. Kostis <lakostis@altlinux.ru> 20150412-alt1
- Initial build based on Fedora package.
