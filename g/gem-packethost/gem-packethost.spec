%define        pkgname packethost

Name:          gem-%pkgname
Version:       0.0.8.1
Release:       alt0.1
Summary:       A Ruby client for the Packet API
License:       GPLv2
Group:         Development/Ruby
Url:           https://www.packet.net
Vcs:           https://github.com/packethost/packet-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A Ruby client for the Packet API.


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
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.8.1-alt0.1
- ^ 0.0.8 -> 0.0.8[.1]

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
