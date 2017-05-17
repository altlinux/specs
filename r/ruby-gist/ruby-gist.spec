%define  pkgname gist

Name: 	 ruby-%pkgname
Version: 4.6.1 
Release: alt1

Summary: Potentially the best command line gister
License: MIT
Group:   Development/Ruby
Url:     https://github.com/defunkt/gist

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
The gist gem provides a gist command that you can use from your terminal to
upload content to https://gist.github.com/.

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
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 4.6.1-alt1
- Initial build in Sisyphus
