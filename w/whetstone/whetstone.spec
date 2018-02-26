Name: whetstone
Version: 1.2
Release: alt2

Summary: Whetstone Double Precision Benchmark
License: Distributable
Group: Monitoring

Url: http://www.netlib.org
Source: whetstone.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

%description
Whetstone Double Precision Benchmark

%prep
%setup -n %name

%build
%make

%install
%makeinstall_std BIN_DIR=%_bindir

%files
%_bindir/*

# TODO: track down precise tarball source

%changelog
* Thu Oct 15 2009 Michael Shigorin <mike@altlinux.org> 1.2-alt2
- built for Sisyphus

* Sat Jul 19 2008 Mikhail Yakshin <greycat@altlinux.org> 2.1-alt1
- Initial build

