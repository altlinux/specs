Name:		python-module-swift-plugin-swift3
Version:	1.7
Release:	alt1
Summary:	The swift3 plugin for Openstack Swift
Group:		Development/Python

License:	ASL 2.0
URL:		https://github.com/fujita/swift3
# git config --global tar.tar.xz.command "xz -c"
# git archive --format=tar.xz --prefix=swift3-1.0.0-#{git_rev}/ #{git_rev}
#Source0:	swift3-1.0.0-#{git_rev}.tar.xz
# URL: https://github.com/fujita/swift3/archive/v1.7.tar.gz
# However, github returns 302 for it. When follow redirect, it returns
# Content-Disposition: attachment; filename=swift3-1.7.tar.gz
Source0:	%{name}-%{version}.tar

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-setuptools

Requires:	openstack-swift >= 1.5.0

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
%setup

%build
%python_build
sed -i 's/\r//' LICENSE

%install
%python_install

%files
%{python_sitelibdir}/swift3-1.7.0-*.egg-info/
%{python_sitelibdir}/swift3/
%doc AUTHORS LICENSE README.md

%changelog
* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 1.7-alt1
- New version

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.0-alt1.git5c74ba04
- Initial release for Sisyphus (based on Fedora)

