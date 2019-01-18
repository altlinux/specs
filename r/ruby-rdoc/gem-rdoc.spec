%define    pkgname rdoc

Name:      ruby-%pkgname
Version:   6.1.1
Release:   alt2

Summary:   RDoc produces HTML and online documentation for Ruby projects.
License:   GPLv2
Group:     Development/Ruby
Url:       https://ruby.github.io/rdoc/
# VCS:     https://github.com/ruby/rdoc.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:    %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
RDoc produces HTML and online documentation for Ruby projects.
RDoc includes the rdoc and ri tools for generating and displaying online
documentation.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.


%package -n rdoc
Summary:   Tool for generation ruby documentation
Group:     Development/Ruby
BuildArch: noarch
Requires:  %name = %version
Obsoletes: ruby-tool-rdoc ruby-tools
Provides:  ruby-tool-rdoc

%description -n rdoc
Tool for generation ruby documentation.


%package -n ri
Summary:   Tool for display descriptions of built-in Ruby methods, classes, and modules
Group:     Development/Ruby
BuildArch: noarch
Requires:  %name = %version
Obsoletes: ruby-tool-rdoc ruby-tools
Conflicts: rdoc <= 1.9.3-alt10

%description -n ri
ri is a command line tool that displays descriptions of built-in Ruby methods,
classes, and modules. For methods, it shows  you  the  calling sequence  and
a description. For classes and modules, it shows a synopsis along with a list
of the methods the class or module implements.


%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
rm -f bin/{console,setup}

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
mkdir -p %buildroot%_bindir/%name
#install -p -m 644 doc/rake.1 %buildroot/%_man1dir
find exe/ -type f -name "*" | while read f; do install -p -m 755 "$f" %buildroot%_bindir; done


%check
%ruby_test

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%files -n rdoc
%_bindir/rdoc

%files -n ri
%_bindir/ri
#%_man1dir/ri.*
#%exclude %_rpmlibdir/%name-doc-ri.filetrigger

%changelog
* Fri Jan 18 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt2
- Added lost provides ruby-tool-rdoc;
- Minor change in rspec.

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- Initial build for Sisyphus, packaged as a gem
