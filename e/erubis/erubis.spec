Name: 	 erubis
Version: 2.7.0 
Release: alt3
 
Summary: A fast and extensible eRuby implementation
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://www.kuwata-lab.com/erubis/
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %name-%version.tar
Patch1:  %name-fix-syntax-errors.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(compiler)$/d
 
%description
Erubis is a fast, secure, and very extensible implementation of eRuby.
It has the following features:
* Very fast, almost three times faster than ERB and about ten percent
  faster than eruby (implemented in C).  * File caching of converted
  Ruby script support.
* Auto escaping (sanitizing) support, it means that '<%= %>' can be
  escaped in default. It is desirable for web application.  * Spaces
  around '<% %>' are trimmed automatically only when '<%' is at the
  beginning of line and '%>' is at the end of line.
* Embedded pattern changeable (default '<% %>'), for example '[% %]' or
  '<? ?>' are available.  * Enable to handle Processing Instructions
  (PI) as embedded pattern (ex. '<?rb ... ?>'). This is desirable for
  XML/HTML than '<% .. %>' because the latter breaks HTML design but
  the former doesn't.
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript).
* Context object available and easy to combine eRuby template with YAML
  datafile (see the below example).  * Print statement available.
* Easy to expand and customize in subclass
* Ruby on Rails support.
* Mod_ruby support.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup
%patch1 -p1
# Remove Rails helper
rm -f lib/erubis/helpers/rails_helper.rb
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
#ruby_test_unit -Ilib:test test
 
%files
%doc README* CHANGES*
%_bindir/%name
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt3
- Fix ruby(compiler) unmet and remove Rails helper

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt2
- Rebuild without ruby-actionpack

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- Initial build for ALT Linux (without tests)
