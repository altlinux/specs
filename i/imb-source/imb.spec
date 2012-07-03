Name: imb-source
Version: 3.2
Release: alt1
Group: Development/Other

Summary: Intel MPI Benchmarks
License: Common Public License
Url: http://software.intel.com/en-us/articles/intel-mpi-benchmarks/
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

Source0: imb-%version.tar

%description
Provide a concise set of benchmarks targeted at measuring the most
important MPI functions.

%prep
%setup -q -n imb-%version

%install

%__mv src imb-%version

install -d -m755 %buildroot%_usrsrc
%__tar -c imb-%version | %__bzip2 -c > \
  %buildroot%_usrsrc/imb-%version.tar.bz2

%files
%_usrsrc/*
%doc doc/*
%doc license/*
%doc ReadMe_first
%doc versions_news/*

%changelog
* Fri Aug 27 2010 Andriy Stepanov <stanv@altlinux.ru> 3.2-alt1
- Build for ALT Linux

