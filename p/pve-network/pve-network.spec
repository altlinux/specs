%def_disable check

Name: pve-network
Summary: PVE SDN package
Version: 0.7.3
Release: alt1
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires: perl pve-cluster >= 6.0 pve-doc-generator
BuildRequires: perl(CPAN/Meta/YAML.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(HTTP/Request.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(NetAddr/IP.pm)
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(Net/Subnet.pm)
BuildRequires: perl(PVE/Cluster.pm)
BuildRequires: perl(PVE/Exception.pm)
BuildRequires: perl(PVE/INotify.pm)
BuildRequires: perl(PVE/JSONSchema.pm)
BuildRequires: perl(PVE/RESTHandler.pm)
BuildRequires: perl(PVE/RPCEnvironment.pm)
BuildRequires: perl(PVE/SafeSyslog.pm)
BuildRequires: perl(PVE/SectionConfig.pm)
BuildRequires: perl(PVE/Tools.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)

%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MPVE::Network::SDN'; export TZ=UTC
%set_perl_req_method relaxed

%description
Proxmox VE's experimental SDN (Software Defined Network)
This package contains the experimental SDN library used by Proxmox VE.

%prep
%setup -q -n %name-%version

%install
%make DESTDIR=%buildroot install

%if_enabled check
%check
make test
%endif

%files
%perl_vendor_privlib/PVE

%changelog
* Fri Mar 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.7.3-alt1
- 0.7.3

* Fri Mar 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Oct 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.7.1-alt1
- Initial build for ALT

