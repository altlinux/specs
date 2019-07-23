%define        pkgname oauth

Name:          ruby-%pkgname
Version:       0.5.4
Release:       alt2
Summary:       OAuth Core Ruby implementation
Group:         Development/Ruby
License:       Distributed
Url:           https://github.com/oauth-xx/oauth-ruby
%vcs           https://github.com/oauth-xx/oauth-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-apache2
BuildRequires: %(eval echo %apache2_apr_buildreq)
BuildRequires: apache2-devel >= 2.2.5
BuildRequires: zlib-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: apache2-httpd-worker
BuildRequires: gcc-c++
BuildRequires: gem(rack)

%description
%summary.

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

%files
%doc README* LICENSE
%_bindir/*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri Jun 28 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt2
- Use Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- Initial gemified build for Sisyphus.
