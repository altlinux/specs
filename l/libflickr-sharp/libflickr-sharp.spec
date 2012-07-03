%define realname flickr-sharp
%define ver_major 2.2
%def_enable doc

Summary: Flickr.Net Library for accessing the Flickr API
Name: lib%{realname}
Version: %ver_major
Release: alt1
License: LGPLv2+
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.codeplex.com/FlickrNet
Source: FlickrNet2.2-Src-48055.zip
Source2: flickrnet.pc
Patch1: flickrnet-assemblyinfo.patch

BuildRequires: mono-mcs mono-devel mono-data mono-web
BuildRequires: rpm-build-mono unzip
BuildRequires: /proc

%description
The Flickr.Net API is a .NET Library for interacting with the Flickr API. It 
can be accessed from any .NET language.

%package devel
Summary: Development files for Flickr.Net
Group: Development/Other
Requires: %name = %version-%release

%description devel
The Flickr.Net API is a .NET Library for interacting with the Flickr API. It 
can be accessed from any .NET language.

The %{name}-devel package contains development files for %{name}.

%prep
%setup -cn FlickrNet -q
cd FlickrNet
%patch1 -p1

%build
cd FlickrNet
gmcs -noconfig -debug -target:library -out:FlickrNet.dll -r:System.dll -r:System.Data.dll -r:System.Drawing.dll -r:System.Xml.dll -r:System.Web.dll -keyfile:FlickrNet.snk "ActivityEvent.cs" "ActivityItem.cs" "ApiKeyRequiredException.cs" "AssemblyInfo.cs" "Auth.cs" "AuthenticationRequiredException.cs" "Blogs.cs" "BoundaryBox.cs" "Cache.cs" "Categories.cs" "Comments.cs" "Contacts.cs" "Context.cs" "DateGranularity.cs" "Enums.cs" "ExifPhoto.cs" "Flickr.cs" "FlickrApiException.cs" "FlickrConfigurationManager.cs" "FlickrConfigurationSettings.cs" "FlickrException.cs" "FlickrWebException.cs" "GeoAccuracy.cs" "GeoPermissions.cs" "Groups.cs" "GroupSearchResults.cs" "Licenses.cs" "Location.cs" "LockFile.cs" "Methods.cs" "PartialSearchOptions.cs" "PersistentCache.cs" "Person.cs" "Photo.cs" "PhotoCounts.cs" "PhotoDates.cs" "PhotoInfo.cs" "PhotoInfoUsage.cs" "PhotoLocation.cs" "PhotoPermissions.cs" "Photos.cs" "PhotoSearchExtras.cs" "PhotoSearchOptions.cs" "PhotoSearchOrder.cs" "PhotoSets.cs" "Place.cs" "Response.cs" "ResponseXmlException.cs" "SafeNativeMethods.cs" "SignatureRequiredException.cs" "Sizes.cs" "Tags.cs" "Uploader.cs" "UploadProgressEvent.cs" "User.cs" "Utils.cs"

%install
cd FlickrNet
gacutil -i FlickrNet.dll -f -package flickrnet -root %buildroot/usr/lib
install -m 0755 -d %buildroot%_libdir/pkgconfig
install -m 0644 -p %SOURCE2 %buildroot%_pkgconfigdir/

%files
%_monodir/flickrnet
%_monogacdir/FlickrNet

%files devel
%_pkgconfigdir/*

%changelog
* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.5-alt5
- move pkgconfig files from main to devel package

* Tue Feb 24 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.5-alt4
- add mono-devel to BuildRequires

* Mon Dec 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.1.5-alt3
- rebuild with new macros _monodocdir
- build with mono-nunit version 2.2

* Tue Apr 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.1.5-alt2
- updated BuildRequires (fix build)

* Tue Jan 15 2008 Alexey Shabalin <shaba@altlinux.ru> 2.1.5-alt1
- Inital release for ALTLinux
