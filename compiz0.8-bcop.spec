%define oname compiz-bcop
%define shortname bcop

Name:		compiz0.8-bcop
Version:	0.8.8
Release:	1
Summary:	BCOP: Compiz Fusion plugin build utility
Group:		System/X11
License:	GPLv2
URL:		http://www.compiz.org/
Source:		http://releases.compiz.org/components/%{oname}/%{oname}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxslt)
Requires:	xsltproc
Conflicts:	compiz > 0.9
BuildArch:	noarch

%description
BCOP: Compiz Fusion plugin build utility.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/%{shortname}
%dir %{_datadir}/%{shortname}
%{_datadir}/%{shortname}/%{shortname}.xslt
%{_datadir}/pkgconfig/%{shortname}.pc

