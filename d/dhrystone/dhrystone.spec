Name: dhrystone
Version: 2.1
Release: alt2

Summary: The BYTE UNIX Benchmarks: Dhrystone
License: Distributable
Group: Monitoring

URL: http://www.byte.com/bmark/
Source: dhrystone.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

%description
The BYTE UNIX Benchmarks: DHRYSTONE by Reinhold P. Weicker

%prep
%setup -n %name

%build
%make

%install
%makeinstall_std BIN_DIR=%_bindir

%files
%_bindir/*

# TODO:
# - update Url:
# - track down precise tarball source

%changelog
* Thu Oct 15 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt2
- built for Sisyphus

* Sat Jul 19 2008 Mikhail Yakshin <greycat@altlinux.org> 2.1-alt1
- Initial build

