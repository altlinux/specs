%define  pkgname heredoc_unindent
 
Name: 	 ruby-%pkgname
Version: 1.1.2 
Release: alt1
 
Summary: Removes leading whitespace from Ruby heredocs
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/adrianomitre/heredoc_unindent
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
This library removes common margin from indented strings, such as the
ones produced by indented heredocs. In other words, it strips out
leading whitespace chars at the beggining of each line, but only as much
as the line with the smallest margin.

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
* Fri May 16 2014 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for ALT Linux
