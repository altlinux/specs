%define  pkgname rbvmomi

Name:    ruby-%pkgname
Version: 1.13.0
Release: alt1

Summary: Ruby interface to the VMware vSphere API.
Summary(ru_RU.UTF8): Ruby интерфейс к API VMware vSphere.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/vmware/rbvmomi

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
RbVmomi is a Ruby interface to the vSphere API. Like the Perl and Java SDKs,
you can use it to manage ESX and vCenter servers. The current release supports
the vSphere 6.5 API. RbVmomi specific documentation is online and is meant
to be used alongside the official documentation.

%description -l ru_RU.UTF8
RbVmomi есть руби-интерфейс к API vSphere, подобный перловому или Явы,
вы можете использовать его для управления серверами ESX и vCenter.
Текущий выпуск поддерживает API vSphere 6.5. Описания специфики RbVmomi естьв пучине,
и может оспользоваться наряду с официальным описанием.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

#%check
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus
