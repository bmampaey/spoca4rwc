#!/usr/bin/env/python

import enum

class _SolarSurface_Area:

    _types_map = {
        'Mm': {'type': float, 'subtype': None},
        'SH': {'type': float, 'subtype': None},
        'Arcsec': {'type': float, 'subtype': None},
        'error': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Mm=None
            , SH=None
            , Arcsec=None
            , error=None
            ):
        self.__Mm = Mm
        self.__SH = SH
        self.__Arcsec = Arcsec
        self.__error = error
    
    def _get_Mm(self):
        return self.__Mm
    def _set_Mm(self, value):
        if not isinstance(value, float):
            raise TypeError("Mm must be float")
        self.__Mm = value
    Mm = property(_get_Mm, _set_Mm)
    
    def _get_SH(self):
        return self.__SH
    def _set_SH(self, value):
        if not isinstance(value, float):
            raise TypeError("SH must be float")
        self.__SH = value
    SH = property(_get_SH, _set_SH)
    
    def _get_Arcsec(self):
        return self.__Arcsec
    def _set_Arcsec(self, value):
        if not isinstance(value, float):
            raise TypeError("Arcsec must be float")
        self.__Arcsec = value
    Arcsec = property(_get_Arcsec, _set_Arcsec)
    
    def _get_error(self):
        return self.__error
    def _set_error(self, value):
        if not isinstance(value, float):
            raise TypeError("error must be float")
        self.__error = value
    error = property(_get_error, _set_error)
    
    def as_dict(self):
        d = dict()
        if self.__Mm is not None:
            d['Mm'] = self.__Mm.as_dict() if hasattr(self.__Mm, 'as_dict') else self.__Mm
        if self.__SH is not None:
            d['SH'] = self.__SH.as_dict() if hasattr(self.__SH, 'as_dict') else self.__SH
        if self.__Arcsec is not None:
            d['Arcsec'] = self.__Arcsec.as_dict() if hasattr(self.__Arcsec, 'as_dict') else self.__Arcsec
        if self.__error is not None:
            d['error'] = self.__error.as_dict() if hasattr(self.__error, 'as_dict') else self.__error
        return d

class FT__SolarSurface_Area:

    _event_type_enum = enum.Enum('_event_type_enum', '_SolarSurface_Area', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': _SolarSurface_Area, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='_SolarSurface_Area'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _SolarSurface_Area):
            raise TypeError("data must be _SolarSurface_Area")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class _HeliographicCoordinate_Stonyhurst:

    _types_map = {
        'Latitude': {'type': float, 'subtype': None},
        'Longitude': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Latitude=None
            , Longitude=None
            ):
        self.__Latitude = Latitude
        self.__Longitude = Longitude
    
    def _get_Latitude(self):
        return self.__Latitude
    def _set_Latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be float")
        self.__Latitude = value
    Latitude = property(_get_Latitude, _set_Latitude)
    
    def _get_Longitude(self):
        return self.__Longitude
    def _set_Longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be float")
        self.__Longitude = value
    Longitude = property(_get_Longitude, _set_Longitude)
    
    def as_dict(self):
        d = dict()
        if self.__Latitude is not None:
            d['Latitude'] = self.__Latitude.as_dict() if hasattr(self.__Latitude, 'as_dict') else self.__Latitude
        if self.__Longitude is not None:
            d['Longitude'] = self.__Longitude.as_dict() if hasattr(self.__Longitude, 'as_dict') else self.__Longitude
        return d

class SPOCA_CoronalHole:

    _types_map = {
        'Min': {'type': list, 'subtype': str},
        '1-Quantils': {'type': list, 'subtype': str},
        'Var': {'type': list, 'subtype': str},
        'Max': {'type': list, 'subtype': str},
        'Mean': {'type': list, 'subtype': str},
        'Skewness': {'type': list, 'subtype': str},
        'Kurtosis': {'type': list, 'subtype': str},
        'Median': {'type': list, 'subtype': str},
        '3-Quantils': {'type': list, 'subtype': str},
        'DetectionTime': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'DetectionTime': 'date-time',
    }

    def __init__(self
            , Min=None
            , 1-Quantils=None
            , Var=None
            , Max=None
            , Mean=None
            , Skewness=None
            , Kurtosis=None
            , Median=None
            , 3-Quantils=None
            , DetectionTime=None
            ):
        self.__Min = Min
        self.__1-Quantils = 1-Quantils
        self.__Var = Var
        self.__Max = Max
        self.__Mean = Mean
        self.__Skewness = Skewness
        self.__Kurtosis = Kurtosis
        self.__Median = Median
        self.__3-Quantils = 3-Quantils
        self.__DetectionTime = DetectionTime
    
    def _get_Min(self):
        return self.__Min
    def _set_Min(self, value):
        if not isinstance(value, list):
            raise TypeError("Min must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Min list valeus must be str")
        self.__Min = value
    Min = property(_get_Min, _set_Min)
    
    def _get_1-Quantils(self):
        return self.__1-Quantils
    def _set_1-Quantils(self, value):
        if not isinstance(value, list):
            raise TypeError("1-Quantils must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("1-Quantils list valeus must be str")
        self.__1-Quantils = value
    1-Quantils = property(_get_1-Quantils, _set_1-Quantils)
    
    def _get_Var(self):
        return self.__Var
    def _set_Var(self, value):
        if not isinstance(value, list):
            raise TypeError("Var must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Var list valeus must be str")
        self.__Var = value
    Var = property(_get_Var, _set_Var)
    
    def _get_Max(self):
        return self.__Max
    def _set_Max(self, value):
        if not isinstance(value, list):
            raise TypeError("Max must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Max list valeus must be str")
        self.__Max = value
    Max = property(_get_Max, _set_Max)
    
    def _get_Mean(self):
        return self.__Mean
    def _set_Mean(self, value):
        if not isinstance(value, list):
            raise TypeError("Mean must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Mean list valeus must be str")
        self.__Mean = value
    Mean = property(_get_Mean, _set_Mean)
    
    def _get_Skewness(self):
        return self.__Skewness
    def _set_Skewness(self, value):
        if not isinstance(value, list):
            raise TypeError("Skewness must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Skewness list valeus must be str")
        self.__Skewness = value
    Skewness = property(_get_Skewness, _set_Skewness)
    
    def _get_Kurtosis(self):
        return self.__Kurtosis
    def _set_Kurtosis(self, value):
        if not isinstance(value, list):
            raise TypeError("Kurtosis must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Kurtosis list valeus must be str")
        self.__Kurtosis = value
    Kurtosis = property(_get_Kurtosis, _set_Kurtosis)
    
    def _get_Median(self):
        return self.__Median
    def _set_Median(self, value):
        if not isinstance(value, list):
            raise TypeError("Median must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("Median list valeus must be str")
        self.__Median = value
    Median = property(_get_Median, _set_Median)
    
    def _get_3-Quantils(self):
        return self.__3-Quantils
    def _set_3-Quantils(self, value):
        if not isinstance(value, list):
            raise TypeError("3-Quantils must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("3-Quantils list valeus must be str")
        self.__3-Quantils = value
    3-Quantils = property(_get_3-Quantils, _set_3-Quantils)
    
    def _get_DetectionTime(self):
        return self.__DetectionTime
    def _set_DetectionTime(self, value):
        if not isinstance(value, str):
            raise TypeError("DetectionTime must be str")
        self.__DetectionTime = value
    DetectionTime = property(_get_DetectionTime, _set_DetectionTime)
    
    def as_dict(self):
        d = dict()
        if self.__Min is not None:
            d['Min'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Min]
        if self.__1-Quantils is not None:
            d['1-Quantils'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__1-Quantils]
        if self.__Var is not None:
            d['Var'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Var]
        if self.__Max is not None:
            d['Max'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Max]
        if self.__Mean is not None:
            d['Mean'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Mean]
        if self.__Skewness is not None:
            d['Skewness'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Skewness]
        if self.__Kurtosis is not None:
            d['Kurtosis'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Kurtosis]
        if self.__Median is not None:
            d['Median'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Median]
        if self.__3-Quantils is not None:
            d['3-Quantils'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__3-Quantils]
        if self.__DetectionTime is not None:
            d['DetectionTime'] = self.__DetectionTime.as_dict() if hasattr(self.__DetectionTime, 'as_dict') else self.__DetectionTime
        return d

class FT_SPOCA_CoronalHole:

    _event_type_enum = enum.Enum('_event_type_enum', 'SPOCA_CoronalHole', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': SPOCA_CoronalHole, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='SPOCA_CoronalHole'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, SPOCA_CoronalHole):
            raise TypeError("data must be SPOCA_CoronalHole")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class _HeliographicCoordinate_Carrington:

    _types_map = {
        'Latitude': {'type': float, 'subtype': None},
        'Longitude': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Latitude=None
            , Longitude=None
            ):
        self.__Latitude = Latitude
        self.__Longitude = Longitude
    
    def _get_Latitude(self):
        return self.__Latitude
    def _set_Latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be float")
        self.__Latitude = value
    Latitude = property(_get_Latitude, _set_Latitude)
    
    def _get_Longitude(self):
        return self.__Longitude
    def _set_Longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be float")
        self.__Longitude = value
    Longitude = property(_get_Longitude, _set_Longitude)
    
    def as_dict(self):
        d = dict()
        if self.__Latitude is not None:
            d['Latitude'] = self.__Latitude.as_dict() if hasattr(self.__Latitude, 'as_dict') else self.__Latitude
        if self.__Longitude is not None:
            d['Longitude'] = self.__Longitude.as_dict() if hasattr(self.__Longitude, 'as_dict') else self.__Longitude
        return d

class CoronalHole:

    _Provider_enum = enum.Enum('_Provider_enum', '+Provider_Catania +Provider_NOAA +Provider_USET +Provider_UKMO +Provider_KSO', module=__name__)
    _types_map = {
        'Polarity': {'type': str, 'subtype': None},
        'Provider': {'type': str, 'subtype': None},
        'EndTime': {'type': str, 'subtype': None},
        'Detections': {'type': list, 'subtype': None},
        'BeginTime': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'Polarity': 'date-time',
        'EndTime': 'date-time',
        'BeginTime': 'date-time',
    }

    def __init__(self
            , Polarity=None
            , Provider=None
            , EndTime=None
            , Detections=None
            , BeginTime=None
            ):
        self.__Polarity = Polarity
        self.__Provider = Provider
        self.__EndTime = EndTime
        self.__Detections = Detections
        self.__BeginTime = BeginTime
    
    def _get_Polarity(self):
        return self.__Polarity
    def _set_Polarity(self, value):
        if not isinstance(value, str):
            raise TypeError("Polarity must be str")
        self.__Polarity = value
    Polarity = property(_get_Polarity, _set_Polarity)
    
    def _get_Provider(self):
        return self.__Provider
    def _set_Provider(self, value):
        if not isinstance(value, str):
            raise TypeError("Provider must be str")
        if value in self._Provider_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _Provider_enum list".format(value))
    Provider = property(_get_Provider, _set_Provider)
    
    def _get_EndTime(self):
        return self.__EndTime
    def _set_EndTime(self, value):
        if not isinstance(value, str):
            raise TypeError("EndTime must be str")
        self.__EndTime = value
    EndTime = property(_get_EndTime, _set_EndTime)
    
    def _get_Detections(self):
        return self.__Detections
    def _set_Detections(self, value):
        if not isinstance(value, list):
            raise TypeError("Detections must be list")
        self.__Detections = value
    Detections = property(_get_Detections, _set_Detections)
    
    def _get_BeginTime(self):
        return self.__BeginTime
    def _set_BeginTime(self, value):
        if not isinstance(value, str):
            raise TypeError("BeginTime must be str")
        self.__BeginTime = value
    BeginTime = property(_get_BeginTime, _set_BeginTime)
    
    def as_dict(self):
        d = dict()
        if self.__Polarity is not None:
            d['Polarity'] = self.__Polarity.as_dict() if hasattr(self.__Polarity, 'as_dict') else self.__Polarity
        if self.__Provider is not None:
            d['Provider'] = self.__Provider.as_dict() if hasattr(self.__Provider, 'as_dict') else self.__Provider
        if self.__EndTime is not None:
            d['EndTime'] = self.__EndTime.as_dict() if hasattr(self.__EndTime, 'as_dict') else self.__EndTime
        if self.__Detections is not None:
            d['Detections'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Detections]
        if self.__BeginTime is not None:
            d['BeginTime'] = self.__BeginTime.as_dict() if hasattr(self.__BeginTime, 'as_dict') else self.__BeginTime
        return d

class FT_CoronalHole:

    _event_type_enum = enum.Enum('_event_type_enum', 'CoronalHole', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': CoronalHole, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='CoronalHole'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, CoronalHole):
            raise TypeError("data must be CoronalHole")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class FT__HeliographicCoordinate_Carrington:

    _event_type_enum = enum.Enum('_event_type_enum', '_HeliographicCoordinate_Carrington', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': _HeliographicCoordinate_Carrington, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='_HeliographicCoordinate_Carrington'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _HeliographicCoordinate_Carrington):
            raise TypeError("data must be _HeliographicCoordinate_Carrington")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class FT__HeliographicCoordinate_Stonyhurst:

    _event_type_enum = enum.Enum('_event_type_enum', '_HeliographicCoordinate_Stonyhurst', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': _HeliographicCoordinate_Stonyhurst, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='_HeliographicCoordinate_Stonyhurst'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _HeliographicCoordinate_Stonyhurst):
            raise TypeError("data must be _HeliographicCoordinate_Stonyhurst")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class _HeliographicCoordinate:

    _types_map = {
        'Carrington': {'type': FT__HeliographicCoordinate_Carrington, 'subtype': None},
        'Stonyhurst': {'type': FT__HeliographicCoordinate_Stonyhurst, 'subtype': None},
        'Time': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'Time': 'date-time',
    }

    def __init__(self
            , Carrington=None
            , Stonyhurst=None
            , Time=None
            ):
        self.__Carrington = Carrington
        self.__Stonyhurst = Stonyhurst
        self.__Time = Time
    
    def _get_Carrington(self):
        return self.__Carrington
    def _set_Carrington(self, value):
        if not isinstance(value, FT__HeliographicCoordinate_Carrington):
            raise TypeError("Carrington must be FT__HeliographicCoordinate_Carrington")
        self.__Carrington = value
    Carrington = property(_get_Carrington, _set_Carrington)
    
    def _get_Stonyhurst(self):
        return self.__Stonyhurst
    def _set_Stonyhurst(self, value):
        if not isinstance(value, FT__HeliographicCoordinate_Stonyhurst):
            raise TypeError("Stonyhurst must be FT__HeliographicCoordinate_Stonyhurst")
        self.__Stonyhurst = value
    Stonyhurst = property(_get_Stonyhurst, _set_Stonyhurst)
    
    def _get_Time(self):
        return self.__Time
    def _set_Time(self, value):
        if not isinstance(value, str):
            raise TypeError("Time must be str")
        self.__Time = value
    Time = property(_get_Time, _set_Time)
    
    def as_dict(self):
        d = dict()
        if self.__Carrington is not None:
            d['Carrington'] = self.__Carrington.as_dict() if hasattr(self.__Carrington, 'as_dict') else self.__Carrington
        if self.__Stonyhurst is not None:
            d['Stonyhurst'] = self.__Stonyhurst.as_dict() if hasattr(self.__Stonyhurst, 'as_dict') else self.__Stonyhurst
        if self.__Time is not None:
            d['Time'] = self.__Time.as_dict() if hasattr(self.__Time, 'as_dict') else self.__Time
        return d

class FT__HeliographicCoordinate:

    _event_type_enum = enum.Enum('_event_type_enum', '_HeliographicCoordinate', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': _HeliographicCoordinate, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='_HeliographicCoordinate'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _HeliographicCoordinate):
            raise TypeError("data must be _HeliographicCoordinate")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class _SolarSurface_BoundingBox:

    _types_map = {
        'LatitudeS': {'type': float, 'subtype': None},
        'LongitudeE': {'type': float, 'subtype': None},
        'LatitudeN': {'type': float, 'subtype': None},
        'LongitudeW': {'type': float, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , LatitudeS=None
            , LongitudeE=None
            , LatitudeN=None
            , LongitudeW=None
            ):
        self.__LatitudeS = LatitudeS
        self.__LongitudeE = LongitudeE
        self.__LatitudeN = LatitudeN
        self.__LongitudeW = LongitudeW
    
    def _get_LatitudeS(self):
        return self.__LatitudeS
    def _set_LatitudeS(self, value):
        if not isinstance(value, float):
            raise TypeError("LatitudeS must be float")
        self.__LatitudeS = value
    LatitudeS = property(_get_LatitudeS, _set_LatitudeS)
    
    def _get_LongitudeE(self):
        return self.__LongitudeE
    def _set_LongitudeE(self, value):
        if not isinstance(value, float):
            raise TypeError("LongitudeE must be float")
        self.__LongitudeE = value
    LongitudeE = property(_get_LongitudeE, _set_LongitudeE)
    
    def _get_LatitudeN(self):
        return self.__LatitudeN
    def _set_LatitudeN(self, value):
        if not isinstance(value, float):
            raise TypeError("LatitudeN must be float")
        self.__LatitudeN = value
    LatitudeN = property(_get_LatitudeN, _set_LatitudeN)
    
    def _get_LongitudeW(self):
        return self.__LongitudeW
    def _set_LongitudeW(self, value):
        if not isinstance(value, float):
            raise TypeError("LongitudeW must be float")
        self.__LongitudeW = value
    LongitudeW = property(_get_LongitudeW, _set_LongitudeW)
    
    def as_dict(self):
        d = dict()
        if self.__LatitudeS is not None:
            d['LatitudeS'] = self.__LatitudeS.as_dict() if hasattr(self.__LatitudeS, 'as_dict') else self.__LatitudeS
        if self.__LongitudeE is not None:
            d['LongitudeE'] = self.__LongitudeE.as_dict() if hasattr(self.__LongitudeE, 'as_dict') else self.__LongitudeE
        if self.__LatitudeN is not None:
            d['LatitudeN'] = self.__LatitudeN.as_dict() if hasattr(self.__LatitudeN, 'as_dict') else self.__LatitudeN
        if self.__LongitudeW is not None:
            d['LongitudeW'] = self.__LongitudeW.as_dict() if hasattr(self.__LongitudeW, 'as_dict') else self.__LongitudeW
        return d

class FT__SolarSurface_BoundingBox:

    _event_type_enum = enum.Enum('_event_type_enum', '_SolarSurface_BoundingBox', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': _SolarSurface_BoundingBox, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='_SolarSurface_BoundingBox'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _SolarSurface_BoundingBox):
            raise TypeError("data must be _SolarSurface_BoundingBox")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class CoronalHoleDetection:

    _Provider_enum = enum.Enum('_Provider_enum', '+Provider_Catania +Provider_NOAA +Provider_USET +Provider_UKMO +Provider_KSO', module=__name__)
    _types_map = {
        'Location': {'type': FT__HeliographicCoordinate, 'subtype': None},
        'CoronalHole': {'type': list, 'subtype': None},
        'BoundingBox': {'type': FT__SolarSurface_BoundingBox, 'subtype': None},
        'Area': {'type': FT__SolarSurface_Area, 'subtype': None},
        'Contour': {'type': list, 'subtype': None},
        'Provider': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , Location=None
            , CoronalHole=None
            , BoundingBox=None
            , Area=None
            , Contour=None
            , Provider=None
            ):
        self.__Location = Location
        self.__CoronalHole = CoronalHole
        self.__BoundingBox = BoundingBox
        self.__Area = Area
        self.__Contour = Contour
        self.__Provider = Provider
    
    def _get_Location(self):
        return self.__Location
    def _set_Location(self, value):
        if not isinstance(value, FT__HeliographicCoordinate):
            raise TypeError("Location must be FT__HeliographicCoordinate")
        self.__Location = value
    Location = property(_get_Location, _set_Location)
    
    def _get_CoronalHole(self):
        return self.__CoronalHole
    def _set_CoronalHole(self, value):
        if not isinstance(value, list):
            raise TypeError("CoronalHole must be list")
        self.__CoronalHole = value
    CoronalHole = property(_get_CoronalHole, _set_CoronalHole)
    
    def _get_BoundingBox(self):
        return self.__BoundingBox
    def _set_BoundingBox(self, value):
        if not isinstance(value, FT__SolarSurface_BoundingBox):
            raise TypeError("BoundingBox must be FT__SolarSurface_BoundingBox")
        self.__BoundingBox = value
    BoundingBox = property(_get_BoundingBox, _set_BoundingBox)
    
    def _get_Area(self):
        return self.__Area
    def _set_Area(self, value):
        if not isinstance(value, FT__SolarSurface_Area):
            raise TypeError("Area must be FT__SolarSurface_Area")
        self.__Area = value
    Area = property(_get_Area, _set_Area)
    
    def _get_Contour(self):
        return self.__Contour
    def _set_Contour(self, value):
        if not isinstance(value, list):
            raise TypeError("Contour must be list")
        self.__Contour = value
    Contour = property(_get_Contour, _set_Contour)
    
    def _get_Provider(self):
        return self.__Provider
    def _set_Provider(self, value):
        if not isinstance(value, str):
            raise TypeError("Provider must be str")
        if value in self._Provider_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _Provider_enum list".format(value))
    Provider = property(_get_Provider, _set_Provider)
    
    def as_dict(self):
        d = dict()
        if self.__Location is not None:
            d['Location'] = self.__Location.as_dict() if hasattr(self.__Location, 'as_dict') else self.__Location
        if self.__CoronalHole is not None:
            d['CoronalHole'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__CoronalHole]
        if self.__BoundingBox is not None:
            d['BoundingBox'] = self.__BoundingBox.as_dict() if hasattr(self.__BoundingBox, 'as_dict') else self.__BoundingBox
        if self.__Area is not None:
            d['Area'] = self.__Area.as_dict() if hasattr(self.__Area, 'as_dict') else self.__Area
        if self.__Contour is not None:
            d['Contour'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Contour]
        if self.__Provider is not None:
            d['Provider'] = self.__Provider.as_dict() if hasattr(self.__Provider, 'as_dict') else self.__Provider
        return d

class _CoronalHoleDetection__SPOCA_CoronalHole_:

    _types_map = {
        'CoronalHoleDetection': {'type': list, 'subtype': None},
        'SPOCA_CoronalHole': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , CoronalHoleDetection=None
            , SPOCA_CoronalHole=None
            ):
        self.__CoronalHoleDetection = CoronalHoleDetection
        self.__SPOCA_CoronalHole = SPOCA_CoronalHole
    
    def _get_CoronalHoleDetection(self):
        return self.__CoronalHoleDetection
    def _set_CoronalHoleDetection(self, value):
        if not isinstance(value, list):
            raise TypeError("CoronalHoleDetection must be list")
        self.__CoronalHoleDetection = value
    CoronalHoleDetection = property(_get_CoronalHoleDetection, _set_CoronalHoleDetection)
    
    def _get_SPOCA_CoronalHole(self):
        return self.__SPOCA_CoronalHole
    def _set_SPOCA_CoronalHole(self, value):
        if not isinstance(value, list):
            raise TypeError("SPOCA_CoronalHole must be list")
        self.__SPOCA_CoronalHole = value
    SPOCA_CoronalHole = property(_get_SPOCA_CoronalHole, _set_SPOCA_CoronalHole)
    
    def as_dict(self):
        d = dict()
        if self.__CoronalHoleDetection is not None:
            d['CoronalHoleDetection'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__CoronalHoleDetection]
        if self.__SPOCA_CoronalHole is not None:
            d['SPOCA_CoronalHole'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__SPOCA_CoronalHole]
        return d

class FT__CoronalHoleDetection__SPOCA_CoronalHole_:

    _event_type_enum = enum.Enum('_event_type_enum', '_CoronalHoleDetection__SPOCA_CoronalHole_', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': _CoronalHoleDetection__SPOCA_CoronalHole_, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='_CoronalHoleDetection__SPOCA_CoronalHole_'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, _CoronalHoleDetection__SPOCA_CoronalHole_):
            raise TypeError("data must be _CoronalHoleDetection__SPOCA_CoronalHole_")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class FT_CoronalHoleDetection:

    _event_type_enum = enum.Enum('_event_type_enum', 'CoronalHoleDetection', module=__name__)
    _types_map = {
        'name': {'type': str, 'subtype': None},
        'event_type': {'type': str, 'subtype': None},
        'data': {'type': CoronalHoleDetection, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , name=None
            , event_type='CoronalHoleDetection'
            , data=None
            ):
        self.__name = name
        self.__event_type = event_type
        self.__data = data
    
    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value
    name = property(_get_name, _set_name)
    
    def _get_event_type(self):
        return self.__event_type
    def _set_event_type(self, value):
        if not isinstance(value, str):
            raise TypeError("event_type must be str")
        if value in self._event_type_enum.__members__:
            self.__type = value
        else:
            raise ValueError("Value {} not in _event_type_enum list".format(value))
    event_type = property(_get_event_type, _set_event_type)
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if not isinstance(value, CoronalHoleDetection):
            raise TypeError("data must be CoronalHoleDetection")
        self.__data = value
    data = property(_get_data, _set_data)
    
    def as_dict(self):
        d = dict()
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__event_type is not None:
            d['event_type'] = self.__event_type.as_dict() if hasattr(self.__event_type, 'as_dict') else self.__event_type
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

class RootObject:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
            ):
    
    def as_dict(self):
        d = dict()
        return d
