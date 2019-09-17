%define        pkgname rbvmomi

Name:          ruby-%pkgname
Version:       2.2.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API.
Summary(ru_RU.UTF8): Ruby интерфейс к API VMware vSphere.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vmware/rbvmomi
%vcs           https://github.com/vmware/rbvmomi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
RbVmomi is a Ruby interface to the vSphere API. Like the Perl and Java SDKs,
you can use it to manage ESX and vCenter servers. The current release supports
the vSphere 6.5 API. RbVmomi specific documentation is online and is meant
to be used alongside the official documentation.

%description   -l ru_RU.UTF8
RbVmomi есть руби-интерфейс к API vSphere, подобный перловому или Явы,
вы можете использовать его для управления серверами ESX и vCenter.
Текущий выпуск поддерживает API vSphere 6.5. Описания специфики RbVmomi есть в
пучине, и может оспользоваться наряду с официальным описанием.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета.


%package       -n rbvmomish
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n rbvmomish
Executable file for %gemname gem.

%description   -n rbvmomish -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%prep
%setup

%build
%ruby_build --use=rbvmomi --alias=rbvmomish

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n rbvmomish
%_bindir/*


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ v2.2.0
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- ^ v2.1.2

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt2
- ^ Ruby Policy 2.0
- - bug closes(#36334)

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus
