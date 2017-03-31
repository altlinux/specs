Name: 	  pcs
Version:  0.99.156
Release:  alt1

Summary:  Pacemaker/Corosync configuration system
License:  GPLv2
Group:    Other
Url: 	  https://github.com/ClusterLabs/pcs

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python rpm-build-ruby ruby python-devel corosync python-module-setuptools

%description
Pacemaker/Corosync configuration system with remote access

%prep
%setup



%install
cd pcs
%makeinstall_std


%files
%_sbindir/*
%python_sitelibdir_noarch/*
/etc/bash_completion.d/*
%_man8dir/*.*


%doc  pcs/CHANGELOG.md pcs/COPYING pcs/README.md

%changelog
* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt1
- Initial release
