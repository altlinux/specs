%define  pkgname octokit.rb
 
Name: 	 ruby-%pkgname
Version: 4.7.0 
Release: alt1
 
Summary: Ruby toolkit for the GitHub API
License: MIT
Group:   Development/Ruby
Url:     https://github.com/octokit/octokit.rb
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
API wrappers should reflect the idioms of the language in which they were
written. Octokit.rb wraps the GitHub API in a flat API client that follows Ruby
conventions and requires little knowledge of REST.

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
%doc *.md
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 4.7.0-alt1
- Initial build in Sisyphus
