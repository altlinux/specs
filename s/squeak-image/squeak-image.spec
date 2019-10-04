Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global image_major 4
%global image_minor 5
%global sources_minor 1
%global image_ver %{image_major}.%{image_minor}
%global image_rel 13680

%if 0%{?image_rel}
%global image_prel .%{?image_rel}
%global image_drel -%{?image_rel}
%endif

%global image_pfullver %{image_ver}%{?image_prel}
%global image_dfullver %{image_ver}%{?image_drel}

Name:           squeak-image
Version:        %{image_pfullver}
Release:        alt1_10
Summary:        The image files for Squeak

License:        MIT
URL:            http://www.squeak.org
Source0:        http://ftp.squeak.org/%{image_ver}/Squeak%{image_dfullver}.zip
Source1:        http://ftp.squeak.org/sources_files/SqueakV41.sources.gz
Source2:        squeak-image-doc.html

Requires:       squeak-vm >= 4.4.7.2357

BuildArch:      noarch
Source44: import.info

%description
This is the standard Squeak image as distributed by sqeak.org.
The Squeak image is split into three interdependent parts,
the .image file, the .changes file, and the .sources file.

%prep
%setup -q -c %{name}-%{version}
cp -p %SOURCE2 .

%build

%install
mkdir -p %{buildroot}%{_datadir}/squeak
# For squeak-image 4.3 (and maybe later) there is a subdir
[ -d Squeak%{image_dfullver} ] && cd Squeak%{image_dfullver}
cp Squeak%{image_dfullver}.image %{buildroot}%{_datadir}/squeak
cp Squeak%{image_dfullver}.changes %{buildroot}%{_datadir}/squeak
zcat %{SOURCE1} >%{buildroot}%{_datadir}/squeak/SqueakV%{image_major}%{sources_minor}.sources
cd %{buildroot}%{_datadir}/squeak
gzip Squeak%{image_dfullver}.image
gzip Squeak%{image_dfullver}.changes
gzip SqueakV%{image_major}%{sources_minor}.sources
ln -sf Squeak%{image_dfullver}.image.gz squeak.image.gz
ln -sf Squeak%{image_dfullver}.changes.gz squeak.changes.gz
ln -s SqueakV%{image_major}%{sources_minor}.sources.gz SqueakV%{image_major}.sources.gz
ln -s SqueakV%{image_major}%{sources_minor}.sources.gz squeak.sources.gz

%files
%doc squeak-image-doc.html
%{_datadir}/squeak/*

%changelog
* Fri Oct 04 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.13680-alt1_10
- new version

