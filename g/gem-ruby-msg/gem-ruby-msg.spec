%define  pkgname ruby-msg

Name:    gem-%pkgname
Version: 1.5.2
Release: alt1

Summary: A library for reading and converting Outlook msg and pst files (mapi message stores)
License: MIT
Group:   Development/Ruby
Url:     https://github.com/aquasync/ruby-msg
# VCS:   https://github.com/aquasync/ruby-msg.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%package -n mapitool
Summary: The command line utility of the library %{pkgname}.
Group: Documentation

BuildArch: noarch

Requires: ruby-gem(%pkgname) = %version

%description -n mapitool
The command line utility, which is allowing to convert individual msg or pst
files to .eml, or to convert a batch to an mbox format file. See mapitool help
for details.

%prep
%setup -n %pkgname-%version
# NOTE patch sources to avoid Encoding::CompatibilityError see http://linuxdata.ru/questions/q54.html
sed 's/part.to_s(opts)/part.to_s(opts).encode("UTF-8", :invalid=>:replace, :undef => :replace, :replace => "")/' -i lib/mapi/mime.rb
# NOTE fix data dir for ALT
sed "s|SUPPORT_DIR = File.dirname(__FILE__) + '/../..'|SUPPORT_DIR = '%_datadir/%name'|" -i lib/mapi/property_set.rb
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
mkdir -p %buildroot%_datadir/%name/data
mv %buildroot%_datadir/*yaml %buildroot%_datadir/%name/data/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#rake test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%files -n mapitool
%_bindir/*
%_datadir/%name/*

%changelog
* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus bumped to 1.5.2
