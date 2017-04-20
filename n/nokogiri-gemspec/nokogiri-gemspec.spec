Name: 	  nokogiri-gemspec
Version:  1.7.1
Release:  alt1

Summary:  Gemspec for static Nokogiri
License:  MIT
Group:    Development/Ruby
Url: 	  http://git.altlinux.org/

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

BuildRequires: ruby-tools rpm-build-ruby

%description
This is a standalone gemspec for nokogiri static package to make nokogiri installed statically to appear in gems

%prep
%setup

%build
export rbVersion=`ruby -e "puts RbConfig::CONFIG[\"ruby_version\"]"`


mkdir -p %buildroot%ruby_libdir/gems/$rbVersion/specifications
cp *.gemspec %buildroot%ruby_libdir/gems/$rbVersion/specifications


%files
%ruby_libdir/gems/*

%changelog
* Thu Apr 20 2017 Denis Medvedev <nbr@altlinux.org> 1.7.1-alt1
- Initial sisyphus release
