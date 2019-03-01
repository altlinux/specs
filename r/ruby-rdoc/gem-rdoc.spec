

%define        pkgname rdoc

Name:          ruby-%pkgname
Version:       6.1.1
Release:       alt3
Summary:       RDoc produces HTML and online documentation for Ruby projects.
License:       GPLv2
Group:         Development/Ruby
Url:           https://ruby.github.io/rdoc/
# VCS:         https://github.com/ruby/rdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
RDoc produces HTML and online documentation for Ruby projects.
RDoc includes the rdoc and ri tools for generating and displaying online
documentation.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n rdoc
Summary:       Tool for generation ruby documentation
Group:         Development/Ruby
BuildArch:     noarch
Requires:      %name = %version
Obsoletes:     ruby-tools
Obsoletes:     ruby-tool-rdoc
Provides:      ruby-tool-rdoc

%description   -n rdoc
Tool for generation ruby documentation.


%package       -n ri
Summary:       Tool for display descriptions of built-in Ruby methods, classes, and modules
Group:         Development/Ruby
BuildArch:     noarch
Requires:      %name = %version
Obsoletes:     ruby-tool-rdoc ruby-tools
Conflicts:     rdoc <= 1.9.3-alt10

%description   -n ri
ri is a command line tool that displays descriptions of built-in Ruby methods,
classes, and modules. For methods, it shows  you  the  calling sequence  and
a description. For classes and modules, it shows a synopsis along with a list
of the methods the class or module implements.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemlibdir
%ruby_gemspec

%files doc
%ruby_gemdocdir

%files         -n rdoc
%_bindir/rdoc

%files         -n ri
%_bindir/ri

%changelog
* Fri Mar 08 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt3
- Use Ruby Policy 2.0.

* Fri Jan 18 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt2
- Added lost provides ruby-tool-rdoc;
- Minor change in rspec.

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- Initial build for Sisyphus, packaged as a gem
