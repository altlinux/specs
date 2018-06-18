%define  pkgname memcached

Name:    ruby-%pkgname
Version: 1.8.0
Release: alt1

Summary: A Ruby interface to the libmemcached C client
License: AFL-3.0
Group:   Development/Ruby
Url:     https://github.com/arthurnn/memcached

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libsasl2-devel
BuildRequires: gnu-config

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
# Replace bundled config.guess and config.sub by files from gnu-config
rm -f ./ext/libmemcached-*/config/config.{guess,sub}
cp -a /usr/share/gnu-config/config.guess ./ext/libmemcached-0.32/config/config.guess
cp -a /usr/share/gnu-config/config.sub ./ext/libmemcached-0.32/config/config.sub
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%%ruby_test_unit -Ilib:ext:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
