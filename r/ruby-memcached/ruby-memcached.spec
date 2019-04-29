%define        pkgname memcached

Name:          ruby-%pkgname
Version:       2.0.0
Release:       alt1
Summary:       A Ruby interface to the libmemcached C client
License:       AFL-3.0
Group:         Development/Ruby
Url:           https://github.com/arthurnn/memcached
# VCS:         https://github.com/arthurnn/memcached.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         allow-use-system-libraries-arg.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libsasl2-devel
BuildRequires: libstdc++-devel
BuildRequires: libmemcached-devel
BuildRequires: gnu-config

%description
An interface to the libmemcached C client.

Features

* clean API
* robust access to all memcached features
* SASL support for the binary protocol
* multiple hashing modes, including consistent hashing
* ludicrous speed, including optional pipelined IO with no_reply

The memcached library wraps the pure-C libmemcached client via SWIG.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup
%patch -p1

%build
%gem_build --use=memcached --version-replace=2.0.0

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Use Ruby Policy 2.0

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
