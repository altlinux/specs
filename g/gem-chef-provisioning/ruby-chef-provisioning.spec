%define        pkgname chef-provisioning

Name:          gem-%pkgname
Version:       2.7.7
Release:       alt1.1
Summary:       A library for creating machines and infrastructures idempotently in Chef.
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-provisioning
Vcs:           https://github.com/chef/chef-provisioning.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version net-ssh ~> 6.0
%gem_replace_version net-scp ~> 3.0
%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Chef Provisioning is a Cookbook and Recipe based approach for managing your
infrastructure. Users can codify their infrastructure and use Chef to converge
their infrastructure to the desired state. It has a plugin model (called
Drivers) to manage different infrastructures, including AWS, Azure and Fog.

Chef Provisioning is maintained according to the Chef Maintenance Policy.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

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


%changelog
* Fri Jul 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt1.1
- ! spec deps and syntax

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt1
- updated (^) 2.7.6 -> 2.7.7
- fixed (!) spec

* Tue Sep 17 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1.1
- fixed (!) spec
- fixed (!) gem dependency

* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- updated (^) 2.7.1 -> 2.7.6
- used (>) Ruby Policy 2.0

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus
