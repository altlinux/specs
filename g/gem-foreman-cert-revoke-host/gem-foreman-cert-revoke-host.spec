%define        _unpackaged_files_terminate_build 1
%define        gemname foreman_cert_revoke_host

Name:          gem-foreman-cert-revoke-host
Version:       0.1.2
Release:       alt1
Summary:       Plugin to revoke host certificate
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/voldmir/foreman_cert_revoke_host
Vcs:           https://github.com/voldmir/foreman_cert_revoke_host.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 12.0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(foreman_cert_revoke_host) = 0.1.2


%description
Plugin to revoke certificate from host properties.


%package       -n gem-foreman-cert-revoke-host-doc
Version:       0.1.2
Release:       alt1
Summary:       Plugin to revoke host certificate documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_cert_revoke_host
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_cert_revoke_host) = 0.1.2

%description   -n gem-foreman-cert-revoke-host-doc
Plugin to revoke host certificate documentation files.

Plugin to revoke certificate from host properties.

%description   -n gem-foreman-cert-revoke-host-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_cert_revoke_host.


%package       -n gem-foreman-cert-revoke-host-devel
Version:       0.1.2
Release:       alt1
Summary:       Plugin to revoke host certificate development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_cert_revoke_host
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_cert_revoke_host) = 0.1.2
Requires:      gem(rake) >= 12.0
Conflicts:     gem(rake) >= 14

%description   -n gem-foreman-cert-revoke-host-devel
Plugin to revoke host certificate development package.

Plugin to revoke certificate from host properties.

%description   -n gem-foreman-cert-revoke-host-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_cert_revoke_host.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-foreman-cert-revoke-host-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-cert-revoke-host-devel
%doc README.md


%changelog
* Thu Mar 16 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
